from worlds.generic.Rules import add_rule


# In-region item gates for individual checks (LOGIC.md "Location rules").
# The region graph already handles everything door-shaped.
LOCATION_RULES = {
    # the demon painting only appears once both clocks are wound (Crank)
    "Mansion - Demon Painting": ["Crank Handle"],
    # the water wheel puzzle (Gemstone) drains the way to the fence
    "Swan Boats - Fence": ["Gemstone"],
    # crane needs the Chain, resin valve needs the Crank; the resin is
    # melted with the dig-site flamethrower prop, fueled from the player's
    # flame ammo — require the Flamethrower so ammo is a sensible expectation
    # (fuel-consumption detail under playtest)
    "Dig Site - Hole": ["Chain", "Crank Handle", "Flamethrower"],
    # the control box (Silver Key) powers the arcade, incl. change machine
    "Arcade - Change Machine": ["Silver Key"],
}


def create_rules(self, location_table):
    multiworld = self.multiworld
    player = self.player

    for loc_name, requires in LOCATION_RULES.items():
        add_rule(multiworld.get_location(loc_name, player),
                 lambda state, _req=tuple(requires), _p=player:
                 all(state.has(item, _p) for item in _req))

    # Goal: defeat Edward Crowley (Victory event at Pool; the client sends
    # StatusUpdate(ClientGoal) when the Ending Sequence scene loads)
    multiworld.completion_condition[player] = \
        lambda state: state.has("Victory", player)

from BaseClasses import LocationProgressType
from worlds.generic.Rules import add_rule
from .Locations import Area

def create_rules(self, location_table):
    multiworld = self.multiworld
    player = self.player

    # Placeholder goal until real progression/goal logic exists: the only
    # progression item in the pool is the Pocket Light.
    multiworld.completion_condition[player] = lambda state: state.has("Pocket Light", player)

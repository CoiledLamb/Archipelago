from BaseClasses import LocationProgressType
from worlds.generic.Rules import add_rule
from .Locations import Area

def create_rules(self, location_table):
    multiworld = self.multiworld
    player = self.player

    # Goal: defeat Edward Crowley (Victory event placed in Regions.py; the
    # client sends StatusUpdate(ClientGoal) when the Ending Sequence loads)
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)

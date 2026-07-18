"""Region graph for Crow Country, from LOGIC.md rev 3 (datamine-verified).

Regions are game scenes (world-side names; the client maps its own scene
names). Entrances are directed; a two-way free door is two entries. Doors
opened from the far side or by in-scene actions are modeled as EVENTS: a
locked event item at the region where the unlock action lives, required by
the gated entrance. Knowledge-only puzzles (keypads, piano, bell, tree
fairy) are free.
"""
from logging import warning
from BaseClasses import Region, ItemClassification
from .Locations import CrowCountryLocation

# All regions. Menu is the AP root; "Park Entrance"/"Restroom" are the
# world-side names for the Entrance/Toilet scenes.
REGIONS = [
    "Menu",
    "Roadside", "Park Entrance", "Station Square", "Gift Shop", "Restroom",
    "Railway", "Fairy Forest", "Cosmic Cosmos", "Mushroom", "Swan Boats",
    "Fairy Pool", "Corridor S", "Save", "Corridor A", "Office Tolman",
    "Restaurant", "Arcade", "Ocean Kingdom", "Submarine", "Storeroom",
    "Boat Ride Dock", "Boat Ride", "Corridor C", "Machine SW",
    "Haunted Hilltop", "Crypt", "Corridor D", "Cell", "Machine SE",
    "Dungeon", "Mansion", "Corridor B", "Theatre", "Office Pike",
    "Office Crow", "Control Room", "Witchwood", "Dig Site",
    "Pre Machine Centre", "Machine Centre", "Mid", "Underground Centre",
    "Ladder", "Underground Lab", "Pool",
    "Underground NE", "Underground NW", "Underground SE", "Underground SW",
    "Break Room",
    "Root Mon", "Root Tue", "Root Wed", "Root Thu", "Root Fri", "Root Sat",
    "Root Sun",
]

# (source, destination, [required item/event names (ANDed)])
# A destination reachable two ways gets two entries (OR).
CONNECTIONS = [
    ("Menu", "Roadside", []),

    # surface free cluster (save-file verified: staff corridors open from
    # the start; Restaurant staff hallway is an unlockable-free swing gate)
    ("Roadside", "Park Entrance", []), ("Park Entrance", "Roadside", []),
    ("Park Entrance", "Station Square", []), ("Station Square", "Park Entrance", []),
    ("Station Square", "Restroom", []), ("Restroom", "Station Square", []),
    ("Station Square", "Fairy Forest", []), ("Fairy Forest", "Station Square", []),
    ("Fairy Forest", "Cosmic Cosmos", []), ("Cosmic Cosmos", "Fairy Forest", []),
    ("Fairy Forest", "Mushroom", []), ("Mushroom", "Fairy Forest", []),
    ("Fairy Forest", "Swan Boats", []), ("Swan Boats", "Fairy Forest", []),
    ("Fairy Forest", "Fairy Pool", []), ("Fairy Pool", "Fairy Forest", []),
    ("Fairy Forest", "Corridor S", []), ("Corridor S", "Fairy Forest", []),
    ("Corridor S", "Save", []), ("Save", "Corridor S", []),
    ("Save", "Corridor A", []), ("Corridor A", "Save", []),
    ("Corridor A", "Arcade", []), ("Arcade", "Corridor A", []),
    ("Corridor A", "Restaurant", []), ("Restaurant", "Corridor A", []),
    ("Arcade", "Ocean Kingdom", []), ("Ocean Kingdom", "Arcade", []),
    ("Restaurant", "Ocean Kingdom", []), ("Ocean Kingdom", "Restaurant", []),
    ("Ocean Kingdom", "Submarine", []), ("Submarine", "Ocean Kingdom", []),
    ("Ocean Kingdom", "Corridor C", []), ("Corridor C", "Ocean Kingdom", []),
    ("Corridor C", "Machine SW", []), ("Machine SW", "Corridor C", []),

    # pond alcove slide door: latch opens from the Corridor A side
    ("Corridor A", "Fairy Pool", []),
    ("Fairy Pool", "Corridor A", ["Slide Door Latch"]),

    # keyed surface doors (reverse traversal is through the now-open door)
    ("Station Square", "Haunted Hilltop", ["Bronze Key"]),
    ("Haunted Hilltop", "Station Square", []),
    ("Station Square", "Railway", ["Bronze Key"]),
    ("Railway", "Station Square", []),
    ("Station Square", "Ocean Kingdom", ["Crank Handle"]),  # winch shortcut
    ("Ocean Kingdom", "Station Square", []),
    ("Station Square", "Gift Shop", ["Silver Key"]),
    ("Gift Shop", "Station Square", []),
    ("Fairy Forest", "Dig Site", ["Bronze Key"]),           # mailbox
    ("Dig Site", "Fairy Forest", []),
    ("Corridor A", "Office Tolman", ["Silver Key"]),
    ("Office Tolman", "Corridor A", []),

    # Hilltop cluster (behind Bronze Key; bell/painting puzzles are free)
    ("Haunted Hilltop", "Crypt", []), ("Crypt", "Haunted Hilltop", []),
    ("Crypt", "Corridor D", []), ("Corridor D", "Crypt", []),
    ("Corridor D", "Haunted Hilltop", []), ("Haunted Hilltop", "Corridor D", []),
    ("Corridor D", "Cell", []), ("Cell", "Corridor D", []),
    ("Corridor D", "Machine SE", []), ("Machine SE", "Corridor D", []),
    ("Haunted Hilltop", "Dungeon", []), ("Dungeon", "Haunted Hilltop", []),
    ("Dungeon", "Corridor B", []), ("Corridor B", "Dungeon", []),
    ("Haunted Hilltop", "Mansion", []), ("Mansion", "Haunted Hilltop", []),
    ("Mansion", "Corridor B", []), ("Corridor B", "Mansion", []),
    ("Corridor B", "Theatre", []), ("Theatre", "Corridor B", []),
    ("Corridor B", "Office Pike", []), ("Office Pike", "Corridor B", []),
    ("Haunted Hilltop", "Witchwood", ["Woeful Mask"]),
    ("Witchwood", "Haunted Hilltop", []),
    ("Corridor B", "Office Crow", ["Golden Key", "Generator Off"]),
    ("Office Crow", "Corridor B", []),
    ("Office Crow", "Control Room", []), ("Control Room", "Office Crow", []),

    # theatre front door is broken open from inside (event in Theatre)
    ("Fairy Forest", "Theatre", ["Theatre Door"]),
    ("Theatre", "Fairy Forest", ["Theatre Door"]),

    # Storeroom door is burned open with the flamethrower (in the pool)
    ("Ocean Kingdom", "Storeroom", ["Flamethrower"]),
    ("Storeroom", "Ocean Kingdom", []),

    # Boat Ride: staff door takes the Golden Key; the public entrance opens
    # once the Root Thu gas leak is stopped
    ("Ocean Kingdom", "Boat Ride Dock", ["Golden Key"]),
    ("Ocean Kingdom", "Boat Ride Dock", ["Gas Vent Off"]),
    ("Boat Ride Dock", "Ocean Kingdom", []),
    ("Boat Ride Dock", "Boat Ride", []), ("Boat Ride", "Boat Ride Dock", []),

    # corridor elevators (Tolman's panel turns them on)
    ("Corridor A", "Underground NW", ["Elevators On"]),
    ("Underground NW", "Corridor A", ["Elevators On"]),
    ("Corridor B", "Underground NE", ["Elevators On"]),
    ("Underground NE", "Corridor B", ["Elevators On"]),
    ("Corridor C", "Underground SW", ["Elevators On"]),
    ("Underground SW", "Corridor C", ["Elevators On"]),
    ("Corridor D", "Underground SE", ["Elevators On"]),
    ("Underground SE", "Corridor D", ["Elevators On"]),

    # central elevator: hidden in the Crow House until the charged Battery
    # makes the mascot walk; runs on the Control Room circuit
    ("Station Square", "Pre Machine Centre",
     ["Battery", "Battery Charged", "Central Elevator On"]),
    ("Pre Machine Centre", "Station Square",
     ["Battery", "Battery Charged", "Central Elevator On"]),

    # underground network
    ("Underground NE", "Underground NW", []), ("Underground NW", "Underground NE", []),
    ("Underground SE", "Underground SW", []), ("Underground SW", "Underground SE", []),
    ("Underground NE", "Underground SE", []), ("Underground SE", "Underground NE", []),
    ("Underground NW", "Underground SW", []), ("Underground SW", "Underground NW", []),
    ("Underground NW", "Break Room", []), ("Break Room", "Underground NW", []),

    # central access pipes only open after Machine Centre has been entered
    # from the front (they test VisitedMachineCentral)
    ("Machine Centre", "Underground SE", []),
    ("Machine Centre", "Underground SW", []),
    ("Underground SE", "Machine Centre", ["Machine Centre Visited"]),
    ("Underground SW", "Machine Centre", ["Machine Centre Visited"]),

    # final zone spine
    ("Pre Machine Centre", "Machine Centre", []),
    ("Machine Centre", "Pre Machine Centre", []),
    ("Machine Centre", "Mid", []), ("Mid", "Machine Centre", []),
    ("Mid", "Underground Centre", []), ("Underground Centre", "Mid", []),
    ("Underground Centre", "Ladder", []), ("Ladder", "Underground Centre", []),
    ("Ladder", "Underground Lab", []),          # one-way drop
    ("Underground Centre", "Underground Lab", []),
    ("Underground Lab", "Underground Centre", ["Glass Vials"]),  # climb
    ("Underground Lab", "Pool", []), ("Pool", "Underground Lab", []),

    # roots hang off the quadrants behind the Break Room's access panel
    ("Underground NE", "Root Sat", ["Root Access"]), ("Root Sat", "Underground NE", []),
    ("Underground NE", "Root Sun", ["Root Access"]), ("Root Sun", "Underground NE", []),
    ("Underground NW", "Root Fri", ["Root Access"]), ("Root Fri", "Underground NW", []),
    ("Underground SE", "Root Mon", ["Root Access"]), ("Root Mon", "Underground SE", []),
    ("Underground SE", "Root Tue", ["Root Access"]), ("Root Tue", "Underground SE", []),
    ("Underground SW", "Root Wed", ["Root Access"]), ("Root Wed", "Underground SW", []),
    ("Underground SW", "Root Thu", ["Root Access"]), ("Root Thu", "Underground SW", []),
]

# (event item name, region it is earned in, [requirements to earn it]).
# All are generator-only: the client never sees them.
EVENTS = [
    ("Slide Door Latch", "Corridor A", []),          # examine latch
    ("Theatre Door", "Theatre", []),                 # walking stick
    ("Elevators On", "Office Tolman", []),           # elevator panel
    ("Root Access", "Break Room", []),               # access panel
    ("Central Elevator On", "Control Room", []),     # numpad 9218
    ("Generator Off", "Root Sun", []),               # generator breaks
    ("Battery Charged", "Root Tue", ["Battery", "Central Elevator On"]),
    ("Gas Vent Off", "Root Thu", ["Data Disk"]),     # gas computer
    ("Machine Centre Visited", "Machine Centre", []),
    ("Victory", "Pool", []),                         # Edward Crowley falls
]


def create_regions(self):
    from . import CrowCountryItem

    player = self.player
    multiworld = self.multiworld

    regions = {name: Region(name, player, multiworld) for name in REGIONS}
    for region in regions.values():
        multiworld.regions.append(region)

    # real locations, by area
    for loc, loc_id in self.location_name_to_id.items():
        area = self.location_name_to_area[loc]
        region = regions.get(area)
        if region is None:
            warning(f"Location {loc} has an invalid area {area}")
            continue
        region.locations.append(CrowCountryLocation(player, loc, loc_id, region))

    # event locations with locked event items
    for event_name, region_name, requires in EVENTS:
        region = regions[region_name]
        event_loc = CrowCountryLocation(player, event_name, None, region)
        event_loc.place_locked_item(CrowCountryItem(
            event_name, ItemClassification.progression, None, player))
        if requires:
            event_loc.access_rule = make_rule(requires, player)
        region.locations.append(event_loc)

    for src, dst, requires in CONNECTIONS:
        name = f"{src} -> {dst}" + (f" ({'+'.join(requires)})" if requires else "")
        regions[src].connect(regions[dst], name,
                             make_rule(requires, player) if requires else None)


def make_rule(requires, player):
    # bind via default args: lambdas in loops share their closure otherwise
    return lambda state, _req=tuple(requires), _p=player: \
        all(state.has(item, _p) for item in _req)

from enum import Enum
from typing import List, TypedDict

from BaseClasses import Location

class Area(str, Enum):
    Roadside = "Roadside"
    ParkEntrance = "Park Entrance"
    StationSquare = "Station Square"
    Restroom = "Restroom"
    FairyForest = "Fairy Forest"
    FairyPool = "Fairy Pool"
    Restaurant = "Restaurant"
    Theatre = "Theatre"
    CorridorC = "Corridor C"
    CorridorD = "Corridor D"
    Mansion = "Mansion"
    SwanBoats = "Swan Boats"
    DigSite = "Dig Site"
    Witchwood = "Witchwood"
    Arcade = "Arcade"
    Dungeon = "Dungeon"
    BoatRide = "Boat Ride"
    UndergroundLab = "Underground Lab"
    Submarine = "Submarine"
    Railway = "Railway"
    GiftShop = "Gift Shop"

class LocationInfo(TypedDict):
    name: str
    id: int
    breakable: bool
    area: Area
    additionalAreas: List[Area]

base_id = 510202400

location_table: List[LocationInfo] = [
    # Roadside
    {"name": "Roadside - Among Trash",
        "id": base_id,
        "breakable": False,
        "area": Area.Roadside,
        "additionalAreas": []},
    
    # Park Entrance
    {"name": "Park Entrance - Flags Base", 
        "id": base_id + 1,
        "breakable": False,
        "area": Area.ParkEntrance,
        "additionalAreas": []},
    {"name": "Park Entrance - Trash Can",
        "id": base_id + 2,
        "breakable": False,
        "area": Area.ParkEntrance,
        "additionalAreas": []},
    
    # Station Square
    {"name": "Station Square - Light Post Base",
        "id": base_id + 3,
        "breakable": False,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Gift Shop Corner",
        "id": base_id + 4,
        "breakable": False,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Shack Corner",
        "id": base_id + 5,
        "breakable": False,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Fence Corner",
        "id": base_id + 6,
        "breakable": False,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Glass Bottle",
        "id": base_id + 7,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Trash Can 1",
        "id": base_id + 8,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Trash Can 2",
        "id": base_id + 9,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Wooden Crate 1",
        "id": base_id + 10,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Wooden Crate 2",
        "id": base_id + 11,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Vending Machine",
        "id": base_id + 12,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    
    # Restroom
    {"name": "Restroom - Sink",
        "id": base_id + 13,
        "breakable": False,
        "area": Area.Restroom,
        "additionalAreas": []},

    # Fairy Forest
    {"name": "Fairy Forest - Mushroom Bushes Right",
        "id": base_id + 14,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Mushroom Bushes Left",
        "id": base_id + 15,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Back Corner",
        "id": base_id + 16,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Glass Bottle",
        "id": base_id + 17,
        "breakable": True,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Trash Can 1",
        "id": base_id + 18,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Trash Can 2",
        "id": base_id + 19,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},

    # Fairy Pool
    {"name": "Fairy Pool - Water Fairy",
        "id": base_id + 20,
        "breakable": False,
        "area": Area.FairyPool,
        "additionalAreas": []},

    # Key-item grant interactables (vanilla spots of the 11 remaining key
    # items; grant anatomy in datamine/KEYITEMS.md, icons/state names in
    # datamine/keyitem_icons.py output)
    {"name": "Restaurant - Treasure Chest",       # vanilla Silver Key
        "id": base_id + 21,
        "breakable": False,
        "area": Area.Restaurant,
        "additionalAreas": []},
    {"name": "Theatre - Fairy Head",              # vanilla Golden Key
        "id": base_id + 22,
        "breakable": False,
        "area": Area.Theatre,
        "additionalAreas": []},
    {"name": "Corridor C - Julie Baron",          # vanilla Golden Key (2nd source)
        "id": base_id + 23,
        "breakable": False,
        "area": Area.CorridorC,
        "additionalAreas": []},
    {"name": "Corridor D - Safe",                 # vanilla Crank Handle
        "id": base_id + 24,
        "breakable": False,
        "area": Area.CorridorD,
        "additionalAreas": []},
    {"name": "Mansion - Demon Painting",          # vanilla Gemstone
        "id": base_id + 25,
        "breakable": False,
        "area": Area.Mansion,
        "additionalAreas": []},
    {"name": "Swan Boats - Fence",                # vanilla Chain
        "id": base_id + 26,
        "breakable": False,
        "area": Area.SwanBoats,
        "additionalAreas": []},
    {"name": "Dig Site - Hole",                   # vanilla Woeful Mask
        "id": base_id + 27,
        "breakable": False,
        "area": Area.DigSite,
        "additionalAreas": []},
    {"name": "Witchwood - Cauldron",              # vanilla Trident
        "id": base_id + 28,
        "breakable": False,
        "area": Area.Witchwood,
        "additionalAreas": []},
    {"name": "Arcade - Change Machine",           # vanilla Data Disk
        "id": base_id + 29,
        "breakable": False,
        "area": Area.Arcade,
        "additionalAreas": []},
    {"name": "Dungeon - Acid Bottle",             # vanilla Acid Bottle
        "id": base_id + 30,
        "breakable": False,
        "area": Area.Dungeon,
        "additionalAreas": []},
    {"name": "Boat Ride - Battery",               # vanilla Battery
        "id": base_id + 31,
        "breakable": False,
        "area": Area.BoatRide,
        "additionalAreas": []},
    {"name": "Underground Lab - Cures",           # vanilla Glass Vials
        "id": base_id + 32,
        "breakable": False,
        "area": Area.UndergroundLab,
        "additionalAreas": []},

    # Weapon grant interactables (bool grants; datamine/weapon_grants.py)
    {"name": "Submarine - Prize Safe",            # vanilla Shotgun (gallery minigame)
        "id": base_id + 33,
        "breakable": False,
        "area": Area.Submarine,
        "additionalAreas": []},
    {"name": "Railway - Flamethrower",            # vanilla Flamethrower
        "id": base_id + 34,
        "breakable": False,
        "area": Area.Railway,
        "additionalAreas": []},
    {"name": "Gift Shop - Gun Drawer",            # vanilla Magnum
        "id": base_id + 35,
        "breakable": False,
        "area": Area.GiftShop,
        "additionalAreas": []},
    {"name": "Gift Shop - Cash Register",         # vanilla Magnum (2nd source, code entry)
        "id": base_id + 36,
        "breakable": False,
        "area": Area.GiftShop,
        "additionalAreas": []},
]

class CrowCountryLocation(Location):
    game: str = "Crow Country"
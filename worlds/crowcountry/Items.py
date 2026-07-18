from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set

class ItemDict(TypedDict):
    name: str
    id: int
    count: int
    classification: ItemClassification

base_id = 510202400

item_table: List[ItemDict] = [
    {"name": "Small Med Kit", "id": base_id + 1, "count": 1, "classification": ItemClassification.filler},
    {"name": "Large Med Kit", "id": base_id + 2, "count": 1, "classification": ItemClassification.filler},
    {"name": "Antidote", "id": base_id + 3, "count": 2, "classification": ItemClassification.filler},
    {"name": "Grenade", "id": base_id + 4, "count": 0, "classification": ItemClassification.useful},
    {"name": "Handgun Ammo", "id": base_id + 5, "count": 3, "classification": ItemClassification.useful},
    {"name": "Shotgun Ammo", "id": base_id + 6, "count": 1, "classification": ItemClassification.useful},
    {"name": "Magnum Ammo", "id": base_id + 7, "count": 0, "classification": ItemClassification.useful},
    {"name": "Pocket Light", "id": base_id + 8, "count": 1, "classification": ItemClassification.progression},
    {"name": "Handgun Laser Sight", "id": base_id + 9, "count": 1, "classification": ItemClassification.useful},
    {"name": "Bronze Key", "id": base_id + 10, "count": 1, "classification": ItemClassification.progression},
    # key items (client writes "item: N" = 1 on receive; numbers in
    # datamine/KEYITEMS.md). Trident has no known lock -> useful.
    {"name": "Silver Key", "id": base_id + 11, "count": 1, "classification": ItemClassification.progression},
    {"name": "Golden Key", "id": base_id + 12, "count": 1, "classification": ItemClassification.progression},
    {"name": "Crank Handle", "id": base_id + 13, "count": 1, "classification": ItemClassification.progression},
    {"name": "Gemstone", "id": base_id + 14, "count": 1, "classification": ItemClassification.progression},
    {"name": "Chain", "id": base_id + 15, "count": 1, "classification": ItemClassification.progression},
    {"name": "Woeful Mask", "id": base_id + 16, "count": 1, "classification": ItemClassification.progression},
    {"name": "Trident", "id": base_id + 17, "count": 1, "classification": ItemClassification.useful},
    {"name": "Data Disk", "id": base_id + 18, "count": 1, "classification": ItemClassification.progression},
    {"name": "Acid Bottle", "id": base_id + 19, "count": 1, "classification": ItemClassification.progression},
    {"name": "Battery", "id": base_id + 20, "count": 1, "classification": ItemClassification.progression},
    {"name": "Glass Vials", "id": base_id + 21, "count": 1, "classification": ItemClassification.progression},
    # weapons (client writes the "item: <gun>" owned-bools). Flamethrower is
    # progression: it burns the Storeroom door and melts the Dig Site resin.
    # Crownade Launcher is NOT pooled: no "item: crownade" global exists —
    # its grant mechanism (CrowQuest secret?) is undecoded.
    {"name": "Shotgun", "id": base_id + 22, "count": 1, "classification": ItemClassification.useful},
    {"name": "Flamethrower", "id": base_id + 23, "count": 1, "classification": ItemClassification.progression},
    {"name": "Magnum", "id": base_id + 24, "count": 1, "classification": ItemClassification.useful},
    {"name": "Flamethrower Ammo", "id": base_id + 25, "count": 0, "classification": ItemClassification.useful},
]

group_table: Dict[str, Set[str]] = {
    "Junk": {"Small Med Kit", "Large Med Kit", "Antidote", "Handgun Ammo",
             "Shotgun Ammo", "Grenade", "Magnum Ammo", "Flamethrower Ammo"},
}
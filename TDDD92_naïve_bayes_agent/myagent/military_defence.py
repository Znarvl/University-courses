from library import *
from typing import List
from myagent.extra import find_start_location, get_unit_type


def move_defence(self: IDABot):
    if len(self.agent_units["Marine"]) > 3:
        if find_start_location(self) == "SE":
            for defence_position in self.defence_position_SE:
                units_at_pos = get_army_unit_at_pos(self, defence_position)
                if len(units_at_pos) < 4:
                    for i in range(4 - len(units_at_pos)):
                        if len(self.agent_units["Marine"]) > 0:
                            marine = self.agent_units["Marine"].pop()
                            self.defence_units["Marine"].append(marine)
                            marine.attack_move(defence_position)
        else:
            for defence_position in self.defence_position_NW:
                units_at_pos = get_army_unit_at_pos(self, defence_position)
                if len(units_at_pos) < 4:
                    for i in range(4 - len(units_at_pos)):
                        if len(self.agent_units["Marine"]) > 0:
                            marine = self.agent_units["Marine"].pop()
                            self.defence_units["Marine"].append(marine)
                            marine.attack_move(defence_position)


def get_defence_unit_at_pos(self: IDABot, position: Point2D) -> List:
    units = []
    for unit in self.defence_units['Marine']:  # type: Unit
        if not unit.has_target and self.map_tools.get_ground_distance(position, unit.position) < 10:
            units.append(unit)
    return units


def get_army_unit_at_pos(self: IDABot, position: Point2D) -> List:
    units = []
    for unit in self.get_my_units():  # type: Unit
        if unit.unit_type.is_combat_unit and self.map_tools.get_ground_distance(position, unit.position) < 10:
            units.append(unit)
    return units


def enter_bunker(self: IDABot):
    bunker_type = UnitType(UNIT_TYPEID.TERRAN_BUNKER, self)
    bunkers = get_unit_type(self, bunker_type)
    for bunker in bunkers:
        if not bunker.is_completed:
            return
    for bunker in bunkers:
        marines_inside_bunker = get_marine_in_bunker(self, bunker.position)
        marines_beside_bunker = get_defence_unit_at_pos(self, bunker.position)
        for i in range(4-len(marines_inside_bunker)):
            if len(marines_beside_bunker) > 0:
                marine = marines_beside_bunker.pop(0)
                marine.right_click(bunker)


def get_marine_in_bunker(self: IDABot, position: Point2D) -> List:
    def squared_distance(position_1, position_2):
        p1 = position_1
        p2 = position_2
        return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

    units = []
    for unit in self.defence_units["Marine"]:  # type: Unit
        if unit.has_target and squared_distance(unit.position, position) < 6:
            units.append(unit)
    return units


def get_bunkers_beside_marine(self: IDABot, position: Point2D) -> List:
    units = []
    for unit in self.get_my_units():  # type: Unit
        if unit.unit_type == UnitType(UNIT_TYPEID.TERRAN_BUNKER, self) \
                and self.map_tools.get_ground_distance(position, unit.position) < 10:
            units.append(unit)
    return units



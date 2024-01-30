from library import IDABot, Unit, UnitType, TypeData, Point2DI, PLAYER_SELF, Point2D, PLAYER_ENEMY, UNIT_TYPEID, BaseLocation
from typing import Optional, List
import math
from myagent.eco import get_command_center_base


def has_addon(bot: IDABot, candidate: Unit, addon_type: UnitType):
    """
    Looks through all units and looks if there is an addon of the type addon_type nearby to the supplied candidate.

    :return: True if the unit "candindate" has an addon of the type "addon_type"
    """
    for unit in bot.get_my_units():
        if unit.unit_type.is_addon and unit.is_alive and unit.is_completed \
                and unit.unit_type == addon_type:
            return True

    return False


def find_producer(bot: IDABot, unit_type: UnitType) -> Optional[Unit]:
    """
    Goes through all units and tries to find a unit which can produce the given unit_type at this very moment. Ignores
    units which non-idle.

    :return: A unit which can build unit_type, None if there is no such unit
    """
    data = bot.tech_tree.get_data(unit_type)  # type: TypeData

    if data.required_addons:
        addon = data.required_addons[0]
    else:
        addon = None

    for candidate in bot.get_my_units():  # type: Unit
        if candidate.unit_type in data.what_builds:
            if addon and not has_addon(bot, candidate, addon):
                continue
            elif candidate.unit_type.is_building and candidate.is_training:
                continue
            elif not candidate.is_completed:
                continue
            elif candidate.unit_type.is_building and candidate.is_flying:
                continue
            elif candidate in bot.building_assignment:
                continue
            else:
                return candidate
    return None


def exists_producer_for(bot: IDABot, unit_type: UnitType) -> bool:
    """
    A faster version of the function find_producer, it only looks if there is a unit which can build the given
    unit_type. It does not check if it is available or even done constructing

    :return: True if there is a unit which might eventually build this unit, False otherwise.
    """
    what_builds = bot.tech_tree.get_data(unit_type).what_builds
    for unit in bot.get_my_units():  # type: Unit
        if unit.is_alive and unit.unit_type in what_builds:
            return True
    return False


def find_refinery_position(bot: IDABot) -> Optional[Point2DI]:
    """
    Goes through each occupied base and checks if there are refineries at each location. If it finds a free spot it
    returns its location, None otherwise.
    """

    refineries = filter(lambda u: u.unit_type.is_refinery, bot.get_my_units())

    for base_location in bot.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        for geyser in base_location.geysers:  # type: Unit
            if not bot.refinery_at_position(geyser.position, refineries) \
                    and not bot.refinery_being_built_at_position(geyser.position):
                return geyser.tile_position

    return None


def calc_closest_base(self: IDABot, point: Point2D):
    """ Goes through each occupied base location and returns the one closest to point."""
    curr_closest = math.inf
    curr_closest_base = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        cc = get_command_center_base(self, base)
        if cc is None:
            continue    # break
        distance = self.map_tools.get_ground_distance(base.position, point)
        if distance < curr_closest:
            curr_closest = distance
            curr_closest_base = base

    return curr_closest_base


def calc_attack_point(self: IDABot, point: Point2D):
    """ Goes through each occupied base location and returns the one closest to point."""
    curr_closest = math.inf
    attack_point = self.base_location_manager.get_player_starting_base_location(PLAYER_ENEMY)
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_ENEMY):
        cc = get_enemy_cc(self, base)
        if cc is None:
            continue  # break
        distance = self.map_tools.get_ground_distance(base.position, point)
        if distance < curr_closest:
            curr_closest = distance
            attack_point = base

    return attack_point.position


def get_enemy_cc(self: IDABot, base_location: BaseLocation):
    for base in self.get_all_units():
        if self.map_tools.get_ground_distance(base.position, base_location.position) < 10 and base.player == PLAYER_ENEMY:
            if base.unit_type == UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self):
                return base


def get_enemy_unit_type(self: IDABot, unit_type: UnitType) -> List:
    units = []
    for unit in self.get_all_units():
        if unit.player == PLAYER_ENEMY:
            if unit.unit_type == unit_type:
                units.append(unit)
    return units


def get_unit_type(self: IDABot, unit_type: UnitType) -> List:
    units = []
    for unit in self.get_my_units():  # type: Unit
        if unit.unit_type == unit_type:
            units.append(unit)
    return units

def get_agent_unit_type(self: IDABot, unit_type: UnitType) -> List:
    units = []
    for unit in self.get_my_units():
        if unit.player == PLAYER_SELF:
            if unit.unit_type == unit_type:
                units.append(unit)
    return units


def find_start_location(self):
    starting_base = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    if self.map_tools.get_ground_distance(starting_base.position,
                                          self.defence_position_SE[0]) < self.map_tools.get_ground_distance(
                                            starting_base.position, self.defence_position_NW[0]):
        return "SE"
    else:
        return "NW"


def remove_dead_unit(self: IDABot):
    if self.step_supply > self.current_supply:
        for key, base in self.bases.items():
            for unitkey, unittype in base.items():
                for unit in unittype:
                    if type(unit) is not list:
                        if not unit.is_alive:
                            self.bases[key][unitkey].remove(unit)
                    else:
                        if not unit[0].is_alive:
                            self.bases[key][unitkey].remove(unit)
                            if unitkey == "scouts":
                                for scout_base in self.bases_to_scout:
                                    if scout_base[1] == unit[1]:
                                        self.bases_to_scout[unit[1]][1] = "not_scouted"
        # ARMY TROOPS

        for key, unittype in self.agent_units.items():
            for unit in unittype:
                if not unit.is_alive:
                    self.agent_units[key].remove(unit)

        for key, unittype in self.defence_units.items():
            for unit in unittype:
                if not unit.is_alive:
                    self.defence_units[key].remove(unit)

        for key, unittype in self.attack_units.items():
            for unit in unittype:
                if not unit.is_alive:
                    self.attack_units[key].remove(unit)
    #Enemy troops
    for key, unittype in self.enemy_units.items():
        for unit in unittype:
            if not unit.is_alive:
                self.enemy_units[key].remove(unit)

    self.step_supply = self.current_supply





def debug(self):
    for key, base in self.bases.items():
        for unit in base["builders"]:
            self.map_tools.draw_text(unit.position, str("builders"))

    for unit in self.defence_units["marines"]:
        self.map_tools.draw_text(unit.position, str("def_marine"))

    pixel_offset = 0.10
    self.map_tools.draw_text_screen(0.010, pixel_offset-0.005, str("Econ Queue:"))
    for each in self.econ_queue.list():
        self.map_tools.draw_text_screen(0.015, pixel_offset, str(each))
        pixel_offset += 0.01

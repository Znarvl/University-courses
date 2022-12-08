from library import *
from typing import List


def can_afford(self: IDABot, unit_type: UnitType):
    """
    Returns True if there are an sufficient amount of minerals, gas and supply to build the given unit_type,
    False otherwise
    """
    return self.step_minerals >= unit_type.mineral_price and self.step_gas >= unit_type.gas_price\
        and (self.max_supply - self.current_supply) >= unit_type.supply_required


def can_afford_upgrade(self: IDABot, upgrade: UpgradeID):
    return self.step_minerals >= self.upgrade_mineral_cost(upgrade) \
           and self.step_gas >= self.upgrade_gas_cost(upgrade)


def get_command_center_base(self: IDABot, base_location: BaseLocation):
    for base in get_my_producers(self, UnitType(UNIT_TYPEID.TERRAN_SCV, self)):
        if self.map_tools.get_ground_distance(base.position, base_location.position) < 10:
            return base


def get_my_producers(self: IDABot, unit_type: UnitType):
    """ Returns a list of units which can build or train units of type unit_type """
    producers = []
    type_data = self.tech_tree.get_data(unit_type)
    what_builds = type_data.what_builds

    for unit in self.get_my_units():
        if unit.unit_type in what_builds:
            producers.append(unit)

    return producers


def get_mineral_fields(self: IDABot, base_location: BaseLocation) -> List[Unit]:
    """
    Given a base_location, this method will find and return a list of all mineral fields (Unit) for that base
    """
    mineral_fields = []
    for mineral_field in base_location.minerals:
        for unit in self.get_all_units():
            if unit.unit_type.is_mineral \
                    and mineral_field.tile_position.x == unit.tile_position.x \
                    and mineral_field.tile_position.y == unit.tile_position.y:
                mineral_fields.append(unit)
    return mineral_fields


def get_geysers(self: IDABot, base_location: BaseLocation) -> List[Unit]:
    """
    Given a base_location, this method will find and return a list of all geysers (Unit) for that base
    """
    geysers = []
    for geyser in base_location.geysers:
        for unit in self.get_all_units():
            if unit.unit_type.is_geyser \
                    and geyser.tile_position.x == unit.tile_position.x \
                    and geyser.tile_position.y == unit.tile_position.y:
                geysers.append(unit)
    return geysers

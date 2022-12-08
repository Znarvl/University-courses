from library import *


def get_my_refineries_base(self: IDABot, base):
    """ Returns a list of all refineries (list of Unit) """
    refineries = []
    for unit in self.get_my_units():
        if unit.unit_type.is_refinery and self.map_tools.get_ground_distance(base.position, unit.position) < 20:
            refineries.append(unit)
    return refineries



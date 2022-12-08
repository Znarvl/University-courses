from library import *
import myagent.gas as gas
from myagent.eco import get_geysers, can_afford
from myagent.extra import calc_closest_base, get_unit_type, has_addon


def build_refinery(self: IDABot):
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        if not self.bases[base.position.x]["refinery0"] or not self.bases[base.position.x]["refinery1"]:
            refinery_type = UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)
            if can_afford(self, refinery_type) and len(self.bases[base.position.x]["mineral_collectors"]) > 0:
                if not self.bases[base.position.x]["gas_collectors0"]:
                    scv = self.bases[base.position.x]["mineral_collectors"].pop()
                    self.bases[base.position.x]["gas_collectors0"].append(scv)
                    geysers = get_geysers(self, base)
                    scv.build_target(refinery_type, geysers[0])
                    self.step_minerals -= 75
                elif not self.bases[base.position.x]["gas_collectors1"]:
                    scv = self.bases[base.position.x]["mineral_collectors"].pop()
                    self.bases[base.position.x]["gas_collectors1"].append(scv)
                    geysers = get_geysers(self, base)
                    scv.build_target(refinery_type, geysers[1])
                    self.step_minerals -= 75
                else:
                    return True


def add_refinery_to_base(self: IDABot):
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        if not self.bases[base.position.x]["refinery0"] or not self.bases[base.position.x]["refinery1"]:
            refineries = gas.get_my_refineries_base(self, base)
            for refinery in refineries:
                if refinery.is_completed:
                    if refinery not in self.bases[base.position.x]["refinery0"] \
                            or refinery in self.bases[base.position.x]["refinery1"]:
                        if not self.bases[base.position.x]["refinery0"]:
                            self.bases[base.position.x]["refinery0"].append(refinery)
                        else:
                            self.bases[base.position.x]["refinery1"].append(refinery)


def build_supply_depot(self: IDABot):
    supply_depot_type = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    build_location = self.building_placer.get_build_location_near(base_location.depot_position,
                                                                  supply_depot_type)
    if self.current_supply + 6 >= self.max_supply:
        return build_building(self, build_location, supply_depot_type)



def is_bunker_at_chokepoint(self: IDABot, position: Point2D):
    for unit in self.get_my_units():  # type: Unit
        if unit.unit_type == UnitType(UNIT_TYPEID.TERRAN_BUNKER, self) \
                and self.map_tools.get_ground_distance(position, unit.position) < 10:
            return True
    return False


def build_barracks(self: IDABot):
    barracks_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    build_location = self.building_placer.get_build_location_near(base_location.depot_position,
                                                                  barracks_type)  # To be changed by Malin
    return build_building(self, build_location, barracks_type)



def build_starport(self: IDABot):
    starport_type = UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)
    factory_type = UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)

    for building in get_unit_type(self, factory_type):
        if not building.is_completed:
            return False
        else:
            build_location = self.building_placer.get_build_location_near(base_location.depot_position, starport_type)
            return build_building(self, build_location, starport_type)


def build_starport_reactor(self: IDABot):
    starport_type = UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)
    starport_reactor_type = UnitType(UNIT_TYPEID.TERRAN_STARPORTREACTOR, self)
    reactor = get_unit_type(self, starport_reactor_type)
    for unit in get_unit_type(self, starport_type):
        if unit.is_alive \
                and not has_addon(self, unit, starport_reactor_type) \
                and can_afford(self, starport_reactor_type) \
                and len(reactor) < 1:
            unit.train(starport_reactor_type)
            return True
        else:
            return False

def build_starport_tech_lab(self: IDABot):
    starport_type = UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)
    starport_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_STARPORTTECHLAB, self)
    tech_lab = get_unit_type(self, starport_tech_lab_type)
    for unit in get_unit_type(self, starport_type):
        if unit.is_alive \
                and not has_addon(self, unit, starport_tech_lab_type) \
                and can_afford(self, starport_tech_lab_type) \
                and len(tech_lab) < 1:
            unit.train(starport_tech_lab_type)
            return True
        else:
            return False



def build_barracks_tech_lab(self: IDABot):
    barracks_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
    barracks_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self)
    tech_labs = get_unit_type(self, barracks_tech_lab_type)
    for unit in get_unit_type(self, barracks_type):
        if unit.is_completed \
                and not has_addon(self, unit, barracks_tech_lab_type) \
                and can_afford(self, barracks_tech_lab_type) \
                and len(tech_labs) < 1:
            unit.train(barracks_tech_lab_type)
            return True

    return False


def build_barracks_reactor(self: IDABot):
    barracks_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
    barracks_reactor_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKSREACTOR, self)
    tech_labs = get_unit_type(self, barracks_reactor_type)
    for unit in get_unit_type(self, barracks_type):
        if unit.is_completed \
                and not has_addon(self, unit, barracks_reactor_type) \
                and can_afford(self, barracks_reactor_type) \
                and len(tech_labs) < 3:
            unit.train(barracks_reactor_type)
            return True

    return False


def build_factory(self: IDABot):
    factory_type = UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)
    factories = get_unit_type(self, factory_type)
    #if self.max_supply > 25 and len(factories) < 3:
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    build_location = self.building_placer.get_build_location_near(base_location.depot_position, factory_type)
    return build_building(self, build_location, factory_type)
    #else:
    #    return False

def build_ghost_academy(self: IDABot):
    factory_type = UnitType(UNIT_TYPEID.TERRAN_GHOSTACADEMY, self)
    factories = get_unit_type(self, factory_type)
    #if self.max_supply > 25 and len(factories) < 3:
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    build_location = self.building_placer.get_build_location_near(base_location.depot_position, factory_type)
    return  build_building(self, build_location, factory_type)
    #else:
    #    return False

def build_armory(self: IDABot):
    factory_type = UnitType(UNIT_TYPEID.TERRAN_ARMORY, self)
    factories = get_unit_type(self, factory_type)
    #if self.max_supply > 25 and len(factories) < 3:
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    build_location = self.building_placer.get_build_location_near(base_location.depot_position, factory_type)
    return build_building(self, build_location, factory_type)

def build_fusion_core(self: IDABot):
    factory_type = UnitType(UNIT_TYPEID.TERRAN_FUSIONCORE, self)
    factories = get_unit_type(self, factory_type)
    #if self.max_supply > 25 and len(factories) < 3:
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    build_location = self.building_placer.get_build_location_near(base_location.depot_position, factory_type)

    return build_building(self, build_location, factory_type)



def build_factory_tech_lab(self: IDABot):
    factory_type = UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)
    factory_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_FACTORYTECHLAB, self)
    tech_labs = get_unit_type(self, factory_tech_lab_type)
    for unit in get_unit_type(self, factory_type):
        if unit.is_alive \
                and not has_addon(self, unit, factory_tech_lab_type) \
                and can_afford(self, factory_tech_lab_type) \
                and len(tech_labs) < 2:
            unit.train(factory_tech_lab_type)
            return True
        else:
            return False


def build_engineering_bay(self: IDABot):
    engineering_bay_type = UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY, self)
    engineering_bays = get_unit_type(self, engineering_bay_type)
    #if self.max_supply > 40 and len(engineering_bays) < 1:
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    build_location = self.building_placer.get_build_location_near(base_location.depot_position,
                                                                  engineering_bay_type)

    return build_building(self, build_location, engineering_bay_type)




def build_command_center(self: IDABot):
    command_center_type = UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)
    for command_center in get_unit_type(self, command_center_type):
        if not command_center.is_completed:
            command_center.right_click(command_center)
            return False

    if can_afford(self, command_center_type):
        build_location = self.base_location_manager.get_next_expansion(PLAYER_SELF)
        base_location = calc_closest_base(self, build_location.position)
        if len(self.bases[base_location.position.x]["mineral_collectors"]) > 0:
            scv = self.bases[base_location.position.x]["mineral_collectors"].pop()
            self.bases[build_location.position.x] = \
                {"mineral_collectors": [],
                 "gas_collectors0": [], "gas_collectors1": [],
                 "builders": [],
                 "refinery0": [], "refinery1": []}
            self.bases[build_location.position.x]["builders"].append(scv)
            scv.build(command_center_type, build_location.depot_position)
            return True
        else:
            return False
    else:
        return False

def build_planetary_fortress(self: IDABot):
    command_center_type = UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)
    planetary_type = UnitType(UNIT_TYPEID.TERRAN_PLANETARYFORTRESS, self)
    for unit in get_unit_type(self, command_center_type):
        if unit.is_alive \
                and not has_addon(self, unit, planetary_type) \
                and can_afford(self, planetary_type):
            unit.train(planetary_type)
            return True
        else:
            return False

def build_orbital_command(self: IDABot):
    command_center_type = UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)
    planetary_type = UnitType(UNIT_TYPEID.TERRAN_ORBITALCOMMAND, self)
    for unit in get_unit_type(self, command_center_type):
        if unit.is_alive \
                and not has_addon(self, unit, planetary_type) \
                and can_afford(self, planetary_type):
            unit.train(planetary_type)
            return True
        else:
            return False

def build_sensor_tower(self: IDABot):
    senstor_tower_type = UnitType(UNIT_TYPEID.TERRAN_SENSORTOWER, self)
    engineering_bays = get_unit_type(self, senstor_tower_type)
    #if self.max_supply > 40 and len(engineering_bays) < 1:
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    build_location = self.building_placer.get_build_location_near(base_location.depot_position,
                                                                  senstor_tower_type)
    return  build_building(self, build_location, senstor_tower_type)

def build_missle_turret(self: IDABot):
    missle_turret_type = UnitType(UNIT_TYPEID.TERRAN_MISSLETURRET, self)
    engineering_bays = get_unit_type(self, missle_turret_type)
    #if self.max_supply > 40 and len(engineering_bays) < 1:
    base_location = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    build_location = self.building_placer.get_build_location_near(base_location.depot_position,
                                                                  missle_turret_type)
    return build_building(self, build_location, missle_turret_type)



def build_building(self: IDABot, build_location: Point2DI, building_type: UnitType):
    for building in get_unit_type(self, building_type):
        if not building.is_completed:
            return False
        else:
            return True
    base_location = calc_closest_base(self, Point2D(build_location.x, build_location.y))
    if can_afford(self, building_type) and len(self.bases[base_location.position.x]["mineral_collectors"]) > 0:
        scv = self.bases[base_location.position.x]["mineral_collectors"].pop()
        self.bases[base_location.position.x]["builders"].append(scv)
        self.step_minerals -= building_type.mineral_price
        self.step_gas -= building_type.gas_price
        scv.build(building_type, build_location)
        return True
    else:
        return False


def bunker_build_at_position(self: IDABot, position):
    for unit in self.get_my_units():  # type: Unit
        if unit.unit_type == UnitType(UNIT_TYPEID.TERRAN_BUNKER, self) \
                and self.map_tools.get_ground_distance(Point2D(position[0], position[1]), unit.position) < 10:
            return True

    return False


def supply_depots_build_at_position(self: IDABot, position: Point2D):
    build = 0
    for unit in self.get_my_units():  # type: Unit
        if unit.unit_type == UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self) \
                and self.map_tools.get_ground_distance(position, unit.position) < 10:
            build += 1
        if build > 1:
            return True
    return False


def build_bunker(self: IDABot):
    bunker_type = UnitType(UNIT_TYPEID.TERRAN_BUNKER, self)
    barracks_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        barracks = get_unit_type(self, barracks_type)
        if len(barracks) < 1:
            return False
        for barrack in barracks:
            if not barrack.is_completed:
                return False
        position = find_choke_point(self, bunker_build_at_position)
        return build_building(self, Point2DI(int(position[0]), int(position[1])), bunker_type)
    else:
        return False


def find_choke_point(self, is_build):
    index = 0
    if index > len(self.chokepoint)-1:
        index = len(self.chokepoint)-1
    position = self.chokepoint[int(index)]
    new_position_find = False
    while not new_position_find:
        if is_build(self, position):
            index += 1
            if index > len(self.chokepoint):
                return position
            if index > len(self.chokepoint)-1:
                index = len(self.chokepoint)-1
            position = self.chokepoint[int(index)]
        else:
            return position


def lower_supply_depot(self):
    for each in get_unit_type(self, UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)):
        if each.is_completed:
            each.morph(UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOTLOWERED, self))
    return True

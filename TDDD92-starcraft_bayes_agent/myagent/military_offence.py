from library import *
from myagent.military_defence import get_army_unit_at_pos
from myagent.extra import calc_attack_point, get_unit_type


# TODO: place all military units to attack group


def find_enemy_start_location(self):
    starting_base = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF)
    if self.map_tools.get_ground_distance(starting_base.position,
                                          self.defence_position_SE[0]) < self.map_tools.get_ground_distance(
        starting_base.position, self.defence_position_NW[0]):
        return "NW"
    else:
        return "SE"


def group_up(self):
    start_loc_SW = Point2D(110, 55)
    start_loc_NW = Point2D(40, 110)
    if len(self.defence_units['Marine']) > 15:
        if find_enemy_start_location(self) == 'NW':
            marine = self.defence_units['Marine'].pop()
            self.attack_units["group"].append(marine)
            marine.attack_move(start_loc_SW)
        else:
            marine = self.defence_units['Marine'].pop()
            self.attack_units["group"].append(marine)
            marine.attack_move(start_loc_NW)

    marauder_type = get_unit_type(self, UnitType(UNIT_TYPEID.TERRAN_MARAUDER, self))
    for marauder in marauder_type:
        if find_enemy_start_location(self) == 'NW':
            if marauder not in self.attack_units['group']:
                self.attack_units['group'].append(marauder)
                marauder.attack_move(start_loc_SW)
        else:
            if marauder not in self.attack_units['group']:
                self.attack_units['group'].append(marauder)
                marauder.attack_move(start_loc_NW)

    medivac_type = get_unit_type(self, UnitType(UNIT_TYPEID.TERRAN_MEDIVAC, self))

    for medivac in medivac_type:
        if find_enemy_start_location(self) == 'NW':
            if medivac not in self.attack_units['group']:
                self.attack_units['group'].append(medivac)
                medivac.attack_move(start_loc_SW)
        else:
            if medivac not in self.attack_units['group']:
                self.attack_units['group'].append(medivac)
                medivac.attack_move(start_loc_NW)


def attack(self):
    if len(self.attack_units['group']) > 30:
        self.attack_units['attack'].extend(self.attack_units['group'])
        self.attack_units['group'].clear()

    if find_enemy_start_location(self) == 'NW':
        attack_pos = Point2D(45, 150)
        if len(self.attack_units['attack']) > 0:
            attack_pos = calc_attack_point(self, self.attack_units['attack'][0].position)

        for marine in self.attack_units['attack']:
            marine.attack_move(attack_pos)
    else:
        attack_pos = Point2D(125, 30)
        if len(self.attack_units['attack']) > 0:
            attack_pos = calc_attack_point(self, self.attack_units['attack'][0].position)

        for marine in self.attack_units['attack']:
            marine.attack_move(attack_pos)


def attack_natural(self):
    pass


def retreat(self):
    '''
    if len(self.attack_units['attack']) <10 and len(self.attack_units['attack']) > 0 :
        self.attack_units['attack'].extend(self.attack_units['group'])
    '''
    pass


'''
def remove_dead_troops(self: IDABot):
    if self.step_supply > self.current_supply:
        for key, army in self.army_units.items():
            for marine in army["marines"]:
                if not marine.is_alive:
                    army["marines"].remove(marine)

        for key, defence in self.defence_units.items():
            for marine in defence["marines"]:
                if not marine.is_alive:
                    defence["marines"].remove(marine)

        for key, attack in self.attack_units.items():
            for marine in attack["marines"]:
                if not marine.is_alive:
                    attack["marines"].remove(marine)
    self.step_supply = self.current_supply
'''
# TODO: Make small harass group? Reaper Banshees etc.

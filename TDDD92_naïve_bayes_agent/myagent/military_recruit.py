from library import *
from myagent.eco import can_afford, get_my_producers
from myagent.extra import has_addon, get_unit_type


def add_unit_to_defence(self: IDABot):
    marine_type = UnitType(UNIT_TYPEID.TERRAN_MARINE, self)
    for marine in get_unit_type(self, marine_type):
        """
        Kommer behöva ändra så det blir "snyggare" kan inte ha en miljard if-satser.
        Detta är endast för att kunna testa tillfällig attack-kod
        Eller får det att göra enklare typ: self.attack_units["vadsomhelst"]?
        """
        if marine not in self.agent_units["Marine"]:
            if marine not in self.defence_units["Marine"]:
                if marine not in self.attack_units["group"]:
                    if marine not in self.attack_units["attack"]:
                        self.agent_units["Marine"].append(marine)

    siege_tank_type = UnitType(UNIT_TYPEID.TERRAN_SIEGETANK, self)
    for tank in get_unit_type(self, siege_tank_type):
        if tank not in self.agent_units["SiegeTank"]:
            if tank not in self.defence_units["SiegeTank"]:
                self.agent_units["SiegeTank"].append(tank)


def train_marines(self: IDABot):
    marine_type = UnitType(UNIT_TYPEID.TERRAN_MARINE, self)
    barrack_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
    if can_afford(self, marine_type):
        for barracks in get_my_producers(self, marine_type):
            if has_addon(self, barracks, UnitType(UNIT_TYPEID.TERRAN_BARRACKSREACTOR, self)) \
                    and can_afford(self, marine_type):
                barracks.train(marine_type)
                self.step_minerals -= marine_type.mineral_price
                self.step_gas -= marine_type.gas_price
                return True
            elif (not barracks.is_training and barracks.is_completed \
                    and not has_addon(self, barracks, UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self))) or \
                    (not barracks.is_training and barracks.is_completed and len(get_unit_type(self, barrack_type)) < 2):
                barracks.train(marine_type)
                self.step_minerals -= marine_type.mineral_price
                self.step_gas -= marine_type.gas_price
                return True




def train_marauders(self: IDABot):
    marauder_type = UnitType(UNIT_TYPEID.TERRAN_MARAUDER, self)
    if can_afford(self, marauder_type):
        for barrack in get_my_producers(self, marauder_type):
            if not barrack.is_training \
                    and has_addon(self, barrack, UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self)):
                barrack.train(marauder_type)
                self.step_minerals -= marauder_type.mineral_price
                self.step_gas -= marauder_type.gas_price
                return True

def train_reapers(self: IDABot):
    reaper_type = UnitType(UNIT_TYPEID.TERRAN_REAPER, self)
    if can_afford(self, reaper_type):
        for barrack in get_my_producers(self, reaper_type):
            if not barrack.is_training:
                barrack.train(reaper_type)
                self.step_minerals -= reaper_type.mineral_price
                self.step_gas -= reaper_type.gas_price
                return True

def train_ghosts(self: IDABot):
    ghost_type = UnitType(UNIT_TYPEID.TERRAN_GHOST, self)
    if can_afford(self, ghost_type):
        for barrack in get_my_producers(self, ghost_type):
            if not barrack.is_training  \
                    and has_addon(self, barrack, UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self)):
                barrack.train(ghost_type)
                self.step_minerals -= ghost_type.mineral_price
                self.step_gas -= ghost_type.gas_price
                return True

def train_vikings(self: IDABot):
    viking_type = UnitType(UNIT_TYPEID.TERRAN_VIKING, self)
    if can_afford(self, viking_type):
        for starport in get_my_producers(self, viking_type):
            if not starport.is_training:
                starport.train(viking_type)
                self.step_minerals -= viking_type.mineral_price
                self.step_gas -= viking_type.gas_price
                return True

def train_vikings(self: IDABot):
    viking_type = UnitType(UNIT_TYPEID.TERRAN_VIKING, self)
    if can_afford(self, viking_type):
        for starport in get_my_producers(self, viking_type):
            if not starport.is_training:
                starport.train(viking_type)
                self.step_minerals -= viking_type.mineral_price
                self.step_gas -= viking_type.gas_price
                return True

def train_medivacs(self: IDABot):
    medivac_type = UnitType(UNIT_TYPEID.TERRAN_MEDIVAC, self)
    if can_afford(self, medivac_type):
        for starport in get_my_producers(self, medivac_type):
            if not starport.is_training:
                starport.train(medivac_type)
                self.step_minerals -= medivac_type.mineral_price
                self.step_gas -= medivac_type.gas_price
                return True


def train_liberators(self: IDABot):
    liberator_type = UnitType(UNIT_TYPEID.TERRAN_LIBERATOR, self)
    if can_afford(self, liberator_type):
        for starport in get_my_producers(self, liberator_type):
            if not starport.is_training:
                starport.train(liberator_type)
                self.step_minerals -= liberator_type.mineral_price
                self.step_gas -= liberator_type.gas_price
                return True

def train_ravens(self: IDABot):
    raven_type = UnitType(UNIT_TYPEID.TERRAN_RAVEN, self)
    starport_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_STARPORTTECHLAB, self)
    if can_afford(self, raven_type):
        for starport in get_my_producers(self, raven_type):
            if not starport.is_training:
                if has_addon(self, starport, starport_tech_lab_type):
                    starport.train(raven_type)
                    self.step_minerals -= raven_type.mineral_price
                    self.step_gas -= raven_type.gas_price
                return True

def train_banshees(self: IDABot):
    banshee_type = UnitType(UNIT_TYPEID.TERRAN_BANSHEE, self)
    starport_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_STARPORTTECHLAB, self)
    if can_afford(self, banshee_type):
        for starport in get_my_producers(self, banshee_type):
            if not starport.is_training:
                if has_addon(self, starport, starport_tech_lab_type):
                    starport.train(banshee_type)
                    self.step_minerals -= banshee_type.mineral_price
                    self.step_gas -= banshee_type.gas_price
                return True

def train_battlecruiser(self: IDABot):
    battlecruiser_type = UnitType(UNIT_TYPEID.TERRAN_BATTLECRUISER, self)
    starport_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_STARPORTTECHLAB, self)
    if can_afford(self, battlecruiser_type):
        for starport in get_my_producers(self, battlecruiser_type):
            if not starport.is_training:
                if has_addon(self, starport, starport_tech_lab_type):
                    starport.train(battlecruiser_type)
                    self.step_minerals -= battlecruiser_type.mineral_price
                    self.step_gas -= battlecruiser_type.gas_price
                return True

def train_tank(self: IDABot):
    tank_type = UnitType(UNIT_TYPEID.TERRAN_SIEGETANK, self)
    factory_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_FACTORYTECHLAB, self)
    if can_afford(self, tank_type):
        for factory in get_my_producers(self, tank_type):
            if not factory.is_training:
                if has_addon(self, factory, factory_tech_lab_type):
                    factory.train(tank_type)
                    self.step_minerals -= tank_type.mineral_price
                    self.step_gas -= tank_type.gas_price
                    return True

def train_hellion(self: IDABot):
    hellion_type = UnitType(UNIT_TYPEID.TERRAN_HELLION, self)
    if can_afford(self, hellion_type):
        for factory in get_my_producers(self, hellion_type):
            if not factory.is_training:
                factory.train(hellion_type)
                self.step_minerals -= hellion_type.mineral_price
                self.step_gas -= hellion_type.gas_price
                return True

def train_cyclone(self: IDABot):
    cyclone_type = UnitType(UNIT_TYPEID.TERRAN_CYCLONE, self)
    factory_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_FACTORYTECHLAB, self)
    if can_afford(self, cyclone_type):
        for factory in get_my_producers(self, cyclone_type):
            if not factory.is_training:
                if has_addon(self, factory, factory_tech_lab_type):
                    factory.train(cyclone_type)
                    self.step_minerals -= cyclone_type.mineral_price
                    self.step_gas -= cyclone_type.gas_price
                    return True

def train_thor(self: IDABot):
    thor_type = UnitType(UNIT_TYPEID.TERRAN_THOR, self)
    factory_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_FACTORYTECHLAB, self)
    if can_afford(self, thor_type):
        for factory in get_my_producers(self, thor_type):
            if not factory.is_training:
                if has_addon(self, factory, factory_tech_lab_type):
                    factory.train(thor_type)
                    self.step_minerals -= thor_type.mineral_price
                    self.step_gas -= thor_type.gas_price
                    return True




def unit_in_list(self: IDABot, unit_list: list, unit_type: UnitType):
    """
    DÖP ALDRIG EN PARAMETER EFTER EN INBYGGD FUNKTION!
    list är en inbyggd funktion, döper ni en parameter till list så skuggar det den inbyggda och orsakar oförutsägbara problem!
    """
    marines = []
    for each in unit_list:
        if each.unit_type == unit_type:
            marines.append(each)
    return marines

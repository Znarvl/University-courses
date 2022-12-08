from library import *
from myagent.extra import get_enemy_unit_type

def get_enemy_scv(self: IDABot):
    SCV_type = UnitType(UNIT_TYPEID.TERRAN_SCV, self)
    for SCV in get_enemy_unit_type(self, SCV_type):
        if SCV not in self.enemy_units["SCV"]:
            self.enemy_units["SCV"].append(SCV)

def get_enemy_marines(self: IDABot):
    marine_type = UnitType(UNIT_TYPEID.TERRAN_MARINE, self)
    for marine in get_enemy_unit_type(self, marine_type):
        if marine not in self.enemy_units["Marine"]:
            self.enemy_units["Marine"].append(marine)

def get_enemy_marauders(self: IDABot):
    marauder_type = UnitType(UNIT_TYPEID.TERRAN_MARAUDER, self)
    for marauder in get_enemy_unit_type(self, marauder_type):
        if marauder not in self.enemy_units["Marauder"]:
            self.enemy_units["Marauder"].append(marauder)

def get_enemy_tanks(self: IDABot):
    tank_type = UnitType(UNIT_TYPEID.TERRAN_SIEGETANK, self)
    for tank in get_enemy_unit_type(self, tank_type):
        if tank not in self.enemy_units["SiegeTank"]:
            self.enemy_units["SiegeTank"].append(tank)

def get_enemy_reapers(self: IDABot):
    reaper_type = UnitType(UNIT_TYPEID.TERRAN_REAPER, self)
    for reaper in get_enemy_unit_type(self, reaper_type):
        if reaper not in self.enemy_units["Reaper"]:
            self.enemy_units["Reaper"].append(reaper)

def get_enemy_ghosts(self: IDABot):
    ghost_type = UnitType(UNIT_TYPEID.TERRAN_GHOST, self)
    for ghost in get_enemy_unit_type(self, ghost_type):
        if ghost not in self.enemy_units["Ghost"]:
            self.enemy_units["Ghost"].append(ghost)

def get_enemy_hellions(self: IDABot):
    hellion_type = UnitType(UNIT_TYPEID.TERRAN_HELLION, self)
    for hellion in get_enemy_unit_type(self, hellion_type):
        if hellion not in self.enemy_units["Hellion"]:
            self.enemy_units["Hellion"].append(hellion)

def get_enemy_cyclones(self: IDABot):
    cyclone_type = UnitType(UNIT_TYPEID.TERRAN_CYCLONE , self)
    for unit in get_enemy_unit_type(self, cyclone_type):
        if unit not in self.enemy_units["Cyclone"]:
            self.enemy_units["Cyclone"].append(unit)

def get_enemy_widow_mines(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_WIDOWMINE, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["WidowMine"]:
            self.enemy_units["WidowMine"].append(unit)

def get_enemy_thors(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_THOR, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Thor"]:
            self.enemy_units["Thor"].append(unit)

def get_enemy_vikings(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_VIKINGFIGHTER, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Viking"]:
            self.enemy_units["Viking"].append(unit)
def get_enemy_medivacs(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_MEDIVAC, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Medivac"]:
            self.enemy_units["Medivac"].append(unit)

def get_enemy_liberators(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_LIBERATOR , self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Liberator"]:
            self.enemy_units["Liberator"].append(unit)

def get_enemy_ravens(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_RAVEN , self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Raven"]:
            self.enemy_units["Raven"].append(unit)

def get_enemy_banshees(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_BANSHEE, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Banshee"]:
            self.enemy_units["Banshee"].append(unit)
def get_enemy_battlecruisers(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_BATTLECRUISER , self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Battlecruiser"]:
            self.enemy_units["Battlecruiser"].append(unit)
def get_enemy_commandcenter(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER , self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["CommandCenter"]:
            self.enemy_units["CommandCenter"].append(unit)

def get_enemy_planetaryfortress(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_PLANETARYFORTRESS, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["PlanetaryFortress"]:
            self.enemy_units["PlanetaryFortress"].append(unit)

def get_enemy_orbitalcommand(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_ORBITALCOMMAND , self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["PlanetaryFortress"]:
            self.enemy_units["PlanetaryFortress"].append(unit)

def get_enemy_supplydepot(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT , self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["SupplyDepot"]:
            self.enemy_units["SupplyDepot"].append(unit)

def get_enemy_refinary(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_REFINERY , self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Refinery"]:
            self.enemy_units["Refinery"].append(unit)

def get_enemy_barrack(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKS , self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Barracks"]:
            self.enemy_units["Barracks"].append(unit)

def get_enemy_engineeringbay(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY , self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["EngineeringBay"]:
            self.enemy_units["EngineeringBay"].append(unit)

def get_enemy_missleturret(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_MISSILETURRET, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["MissileTurret"]:
            self.enemy_units["MissileTurret"].append(unit)

def get_enemy_factory(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Factory"]:
            self.enemy_units["Factory"].append(unit)

def get_enemy_starport(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Starport"]:
            self.enemy_units["Starport"].append(unit)

def get_enemy_armory(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_ARMORY, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["Armory"]:
            self.enemy_units["Armory"].append(unit)

def get_enemy_fusioncore(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_FUSIONCORE, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["FusionCore"]:
            self.enemy_units["FusionCore"].append(unit)

def get_enemy_ghostacademy(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_GHOSTACADEMY, self)
    for unit in get_enemy_unit_type(self, unit_type):
        if unit not in self.enemy_units["GhostAcademy"]:
            self.enemy_units["GhostAcademy"].append(unit)


def get_all_enemy_units(self: IDABot):
    get_enemy_scv(self)
    get_enemy_marines(self)
    get_enemy_marauders(self)
    get_enemy_reapers(self)
    get_enemy_ghosts(self)
    get_enemy_hellions(self)
    get_enemy_tanks(self)
    get_enemy_cyclones(self)
    get_enemy_widow_mines(self)
    get_enemy_thors(self)
    get_enemy_vikings(self)
    get_enemy_medivacs(self)
    get_enemy_liberators(self)
    get_enemy_ravens(self)
    get_enemy_banshees(self)
    get_enemy_battlecruisers(self)
    get_enemy_commandcenter(self)
    get_enemy_planetaryfortress(self)
    get_enemy_orbitalcommand(self)
    get_enemy_supplydepot(self)
    get_enemy_barrack(self)
    get_enemy_engineeringbay(self)
    get_enemy_missleturret(self)
    get_enemy_factory(self)
    get_enemy_starport(self)
    get_enemy_armory(self)
    get_enemy_fusioncore(self)
    get_enemy_ghostacademy(self)








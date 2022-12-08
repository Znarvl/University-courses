from library import *
from myagent.extra import get_agent_unit_type

def scv(self: IDABot):
    SCV_type = UnitType(UNIT_TYPEID.TERRAN_SCV, self)
    for SCV in get_agent_unit_type(self, SCV_type):
        if SCV not in self.agent_units["SCV"]:
            self.agent_units["SCV"].append(SCV)

def marines(self: IDABot):
    marine_type = UnitType(UNIT_TYPEID.TERRAN_MARINE, self)
    for marine in get_agent_unit_type(self, marine_type):
        if marine not in self.agent_units["Marine"]:
            self.agent_units["Marine"].append(marine)

def marauders(self: IDABot):
    marauder_type = UnitType(UNIT_TYPEID.TERRAN_MARAUDER, self)
    for marauder in get_agent_unit_type(self, marauder_type):
        if marauder not in self.agent_units["Marauder"]:
            self.agent_units["Marauder"].append(marauder)

def tanks(self: IDABot):
    tank_type = UnitType(UNIT_TYPEID.TERRAN_SIEGETANK, self)
    for tank in get_agent_unit_type(self, tank_type):
        if tank not in self.agent_units["SiegeTank"]:
            self.agent_units["SiegeTank"].append(tank)

def reapers(self: IDABot):
    reaper_type = UnitType(UNIT_TYPEID.TERRAN_REAPER, self)
    for reaper in get_agent_unit_type(self, reaper_type):
        if reaper not in self.agent_units["Reaper"]:
            self.agent_units["Reaper"].append(reaper)

def ghosts(self: IDABot):
    ghost_type = UnitType(UNIT_TYPEID.TERRAN_GHOST, self)
    for ghost in get_agent_unit_type(self, ghost_type):
        if ghost not in self.agent_units["Ghost"]:
            self.agent_units["Ghost"].append(ghost)

def hellions(self: IDABot):
    hellion_type = UnitType(UNIT_TYPEID.TERRAN_HELLION, self)
    for hellion in get_agent_unit_type(self, hellion_type):
        if hellion not in self.agent_units["Hellion"]:
            self.agent_units["Hellion"].append(hellion)

def cyclones(self: IDABot):
    cyclone_type = UnitType(UNIT_TYPEID.TERRAN_CYCLONE , self)
    for unit in get_agent_unit_type(self, cyclone_type):
        if unit not in self.agent_units["Cyclone"]:
            self.agent_units["Cyclone"].append(unit)

def widow_mines(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_WIDOWMINE, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["WidowMine"]:
            self.agent_units["WidowMine"].append(unit)

def thors(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_THOR, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Thor"]:
            self.agent_units["Thor"].append(unit)

def vikings(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_VIKINGFIGHTER, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Viking"]:
            self.agent_units["Viking"].append(unit)
def medivacs(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_MEDIVAC, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Medivac"]:
            self.agent_units["Medivac"].append(unit)

def liberators(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_LIBERATOR , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Liberator"]:
            self.agent_units["Liberator"].append(unit)

def ravens(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_RAVEN , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Raven"]:
            self.agent_units["Raven"].append(unit)

def banshees(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_BANSHEE, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Banshee"]:
            self.agent_units["Banshee"].append(unit)
def battlecruisers(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_BATTLECRUISER , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Battlecruiser"]:
            self.agent_units["Battlecruiser"].append(unit)

def commandcenter(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["CommandCenter"]:
            self.agent_units["CommandCenter"].append(unit)

def planetaryfortress(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_PLANETARYFORTRESS , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["PlanetaryFortress"]:
            self.agent_units["PlanetaryFortress"].append(unit)

def orbitalcommand(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_ORBITALCOMMAND , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["PlanetaryFortress"]:
            self.agent_units["PlanetaryFortress"].append(unit)

def supplydepot(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["SupplyDepot"]:
            self.agent_units["SupplyDepot"].append(unit)

def refinary(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_REFINERY , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Refinery"]:
            self.agent_units["Refinery"].append(unit)

def barrack(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKS , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Barracks"]:
            self.agent_units["Barracks"].append(unit)

def engineeringbay(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY , self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["EngineeringBay"]:
            self.agent_units["EngineeringBay"].append(unit)

def missleturret(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_MISSILETURRET, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["MissileTurret"]:
            self.agent_units["MissileTurret"].append(unit)

def factory(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Factory"]:
            self.agent_units["Factory"].append(unit)

def starport(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Starport"]:
            self.agent_units["Starport"].append(unit)

def armory(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_ARMORY, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["Armory"]:
            self.agent_units["Armory"].append(unit)

def fusioncore(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_FUSIONCORE, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["FusionCore"]:
            self.agent_units["FusionCore"].append(unit)

def ghostacademy(self: IDABot):
    unit_type = UnitType(UNIT_TYPEID.TERRAN_GHOSTACADEMY, self)
    for unit in get_agent_unit_type(self, unit_type):
        if unit not in self.agent_units["GhostAcademy"]:
            self.agent_units["GhostAcademy"].append(unit)

def get_all_units(self: IDABot):
    scv(self)
    marines(self)
    marauders(self)
    reapers(self)
    ghosts(self)
    hellions(self)
    tanks(self)
    cyclones(self)
    widow_mines(self)
    thors(self)
    vikings(self)
    medivacs(self)
    liberators(self)
    ravens(self)
    banshees(self)
    battlecruisers(self)
    commandcenter(self)
    planetaryfortress(self)
    orbitalcommand(self)
    supplydepot(self)
    barrack(self)
    engineeringbay(self)
    missleturret(self)
    factory(self)
    starport(self)
    armory(self)
    fusioncore(self)
    ghostacademy(self)


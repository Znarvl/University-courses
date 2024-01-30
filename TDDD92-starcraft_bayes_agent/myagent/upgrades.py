from library import *
from myagent.eco import can_afford_upgrade
from myagent.extra import get_unit_type


def research_upgrades(self: IDABot, upgrade: UpgradeID, building: UnitType):
    """

    :param self: An instance of IDABot
    :param upgrade: An UpgradeID matching the upgrade to be researched
    :param building: A UnitType that is a producer of upgrade
    """
    for building in get_unit_type(self, building):
        if can_afford_upgrade(self, upgrade) and building.is_idle:
            building.research(upgrade)
            self.step_minerals -= self.upgrade_mineral_cost(upgrade)
            self.step_gas -= self.upgrade_gas_cost(upgrade)
            break


def upgrade_infantry_armour(self: IDABot):
    """

    :param self: An instance of IDABot
    """
    armour_upgrade_type1 = UpgradeID(UPGRADE_ID.TERRANINFANTRYARMORSLEVEL1)
    armour_upgrade_type2 = UpgradeID(UPGRADE_ID.TERRANINFANTRYARMORSLEVEL2)
    armour_upgrade_type3 = UpgradeID(UPGRADE_ID.TERRANINFANTRYARMORSLEVEL3)
    engineering_bay_type = UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY, self)
    if can_afford_upgrade(self, armour_upgrade_type1):
        research_upgrades(self, armour_upgrade_type1, engineering_bay_type)
    elif can_afford_upgrade(self, armour_upgrade_type2):
        research_upgrades(self, armour_upgrade_type2, engineering_bay_type)
    elif can_afford_upgrade(self, armour_upgrade_type3):
        research_upgrades(self, armour_upgrade_type3, engineering_bay_type)


def upgrade_infantry_weapons(self: IDABot):
    """

    :param self: An instance of IDABot
    """
    weapons_upgrade_type1 = UpgradeID(UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL1)
    weapons_upgrade_type2 = UpgradeID(UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL2)
    weapons_upgrade_type3 = UpgradeID(UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL3)
    engineering_bay_type = UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY, self)
    if can_afford_upgrade(self, weapons_upgrade_type1):
        research_upgrades(self, weapons_upgrade_type1, engineering_bay_type)
    elif can_afford_upgrade(self, weapons_upgrade_type2):
        research_upgrades(self, weapons_upgrade_type2, engineering_bay_type)
    elif can_afford_upgrade(self, weapons_upgrade_type3):
        research_upgrades(self, weapons_upgrade_type3, engineering_bay_type)


def research_combat_shields(self: IDABot):
    """
    Get the UpgradeID of Marine Combat Shields, and the UnitType of a Barracks Tech Lab and sends it to
    research_upgrades()
    :param self: An instance of IDABot
    """
    combat_shields_type = UpgradeID(UPGRADE_ID.SHIELDWALL)
    barracks_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self)
    research_upgrades(self, combat_shields_type, barracks_tech_lab_type)


def research_concussive_shells(self: IDABot):
    """
    Get the UpgradeID of Marauder Concussive Shells, and the UnitType of a Barracks Tech Lab and sends it to
    research_upgrades()
    :param self: An instance of IDABot
    """
    concussive_shells_type = UpgradeID(UPGRADE_ID.PUNISHERGRENADES)
    barracks_tech_lab_type = UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self)
    research_upgrades(self, concussive_shells_type, barracks_tech_lab_type)

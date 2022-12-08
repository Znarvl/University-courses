from typing import Optional
from library import *
from myagent.extra import *

import myagent.worker as worker
import myagent.building as building
import myagent.military_recruit as military_recruit
import myagent.military_defence as military_defence
import myagent.military_offence as military_offence
import myagent.enemy_units as enemy_units
import myagent.scout as scout
import myagent.upgrades as upgrades
import myagent.priority_queue as priority_queue
import myagent.agent_units as agent_units
import myagent.naive_bayes as bayes


class MyAgent(IDABot):
    def __init__(self):
        IDABot.__init__(self)
        self.time = 0
        self.econ_queue = priority_queue.Priority_queue()
        priority_queue.load_econ_queue(self)
        self.latest_build_number = 999


        self.bases = {}
        self.agent_units = {"SCV": [], "Marine": [], "Marauder": [], "Reaper": [], "Ghost": [],
                            "Hellion": [], "SiegeTank": [], "Cyclone": [], "WidowMine": [], "Thor": [],
                            "Viking": [], "Medivac": [], "Liberator": [], "Raven": [], "Banshee": [],
                            "Battlecruiser": [], "CommandCenter": [], "PlanetaryFortress": [], "OrbitalCommand": [], "SupplyDepot": [],
            'Barracks': [], 'EngineeringBay': [], "Bunker": [],
                          "MissileTurret": [], "Factory": [], "Starport": []
            ,"Armory": [], "FusionCore": [], "GhostAcademy": []}

        self.defence_units = {"Marine": [], "SiegeTank": []}

        self.enemy_units = {"SCV": [], "Marine": [], "Marauder": [], "Reaper": [], "Ghost": [],
                            "Hellion": [], "SiegeTank": [], "Cyclone": [], "WidowMine": [], "Thor": [],
                            "Viking": [], "Medivac": [], "Liberator": [], "Raven": [], "Banshee": [],
                            "Battlecruiser": [], "CommandCenter": [], "PlanetaryFortress": [], "OrbitalCommand": [], "SupplyDepot": [],
            'Barracks': [], 'EngineeringBay': [], "Bunker": [],
                          "MissileTurret": [], "Factory": [], "Starport": [], "Armory": [], "FusionCore": [], "GhostAcademy": []}
        self.attack_units = {'group': [], 'attack': []}

        self.bases_to_scout = []
        self.step_minerals = 0
        self.step_gas = 0
        self.step_supply = 0
        self.defence_position = 0

        self.defence_position_SE = [Point2D(115, 43), Point2D(114, 57), Point2D(105, 64), Point2D(89, 50),
                                    Point2D(78, 33)]
        self.chokepoint_SE = [Point2D(115, 43), Point2D(114, 57), Point2D(107, 67), Point2D(89, 50),
                                    Point2D(78, 33)]
        self.defence_position_NW = [Point2D(37, 125), Point2D(36, 111), Point2D(47, 106), Point2D(63, 119),
                                    Point2D(74, 135)]
        self.chokepoint_NW = [Point2D(36, 124), Point2D(36, 111), Point2D(44, 100), Point2D(63, 119),
                                    Point2D(74, 135)]

    def on_game_start(self):
        IDABot.on_game_start(self)
        priority_queue.load_econ_queue(self)

    def on_step(self):
        IDABot.on_step(self)
        self.step_minerals = self.minerals
        self.step_gas = self.gas
        worker.add_base_dicts(self)
        remove_dead_unit(self)
        building.add_refinery_to_base(self)
        enemy_units.get_all_enemy_units(self)
        agent_units.get_all_units(self)
        remove_dead_unit(self)
        if self.time % 10 == 0:
            priority_queue.execute_econ_queue(self)
            building.build_refinery(self)
            building.build_supply_depot(self)
            building.build_barracks_tech_lab(self)
            worker.worker_collect_minerals(self)
            building.lower_supply_depot(self)
            military_defence.move_defence(self)
            worker.train_workers(self)
            military_offence.group_up(self)
            military_offence.attack(self)
            military_recruit.add_unit_to_defence(self)
            upgrades.upgrade_infantry_armour(self)
            upgrades.upgrade_infantry_weapons(self)
            upgrades.research_combat_shields(self)
            upgrades.research_concussive_shells(self)
            worker.worker_collect_gas(self)
        if self.time % 40 == 0:
            scout.maintain_scouting(self)
        if self.time % 350 == 0:
            enemyDictLength = {key: len(value) for key, value in self.enemy_units.items()}
            agentDictLength = {key: len(value) for key, value in self.agent_units.items()}
            if sum(enemyDictLength.values()) > 15: # We need to have observervations of enemy before using naive bayes
                build_order, build_number = bayes.naive_bayes(agentDictLength, enemyDictLength)
                if isinstance(build_order, list):
                    print("Agents total state: " + str(agentDictLength.values()))
                    print("Enemy total state: " + str(enemyDictLength.values()))
                    if self.latest_build_number != build_number:
                        print("New build order from list: " + str(build_number))
                        print("New build order list:")
                        print(build_order)
                        self.latest_build_number = build_number
                        self.econ_queue.flush() #Removes old list of build order
                        self.econ_queue.enqueueList(build_order) #add new list of build order
                    if self.latest_build_number == build_number:
                        if len(build_order) != self.econ_queue.size(): #Sometimes elements get lost in cyberspace, if they do this we re-append them to the game
                            print("Same build but adding lost elements: " + str(build_number))
                            self.econ_queue.flush()
                            self.econ_queue.enqueueList(build_order)
        self.time += 1

import random
from myagent.eco import get_command_center_base, get_mineral_fields, can_afford
from library import *


def add_base_dicts(self: IDABot):
    if not self.bases:
        cc = get_command_center_base(self, self.base_location_manager.get_player_starting_base_location(PLAYER_SELF))
        cc.right_click(cc)
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        try:
            self.bases[base.position.x]
        except KeyError:
            self.bases[base.position.x] = \
                {"mineral_collectors": [],
                 "gas_collectors0": [], "gas_collectors1": [],
                 "builders": [],
                 "refinery0": [], "refinery1": []}


def get_my_workers_base(self: IDABot, base: BaseLocation):
    workers = []
    for unit in self.get_my_units():  # type: Unit
        if unit.unit_type.is_worker and self.map_tools.get_ground_distance(base.position, unit.position) < 20:
            workers.append(unit)

    return workers


def worker_collect_minerals(self: IDABot):
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        for worker in self.bases[base.position.x]["builders"]:
            if worker.is_idle:
                self.bases[base.position.x]["builders"].remove(worker)
                self.bases[base.position.x]["mineral_collectors"].append(worker)
                if len(get_mineral_fields(self, base)) > 0:
                    worker.right_click(random.choice(get_mineral_fields(self, base)))

    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        workers = get_my_workers_base(self, base)
        for worker in workers:
            if worker.is_idle:
                if worker not in self.bases[base.position.x]["mineral_collectors"]:
                    if worker not in self.bases[base.position.x]["gas_collectors0"]:
                        if worker not in self.bases[base.position.x]["gas_collectors1"]:
                            if worker not in self.bases[base.position.x]["builders"]:
                                self.bases[base.position.x]["mineral_collectors"].append(worker)
                                if len(get_mineral_fields(self, base)) > 0:
                                    worker.right_click(random.choice(get_mineral_fields(self, base)))


def train_workers(self: IDABot):
    scv_type = UnitType(UNIT_TYPEID.TERRAN_SCV, self)
    if not can_afford(self, scv_type):
        return
    for base_location in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        base = get_command_center_base(self, base_location)
        if base is None:
            return
        if base.is_training:
            return
        if (len(self.bases[base_location.position.x]["mineral_collectors"]) +
                len(self.bases[base_location.position.x]["builders"])) < len(get_mineral_fields(self, base_location))*2:
            base.train(scv_type)


def worker_collect_gas(self: IDABot):
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        if len(self.bases[base.position.x]["mineral_collectors"]) > 3:
            if self.bases[base.position.x]["refinery0"] and len(self.bases[base.position.x]["gas_collectors0"]) < 3:
                for i in range(3-len(self.bases[base.position.x]["gas_collectors0"])):
                    if len(self.bases[base.position.x]["mineral_collectors"]) > 0:
                        scv = self.bases[base.position.x]["mineral_collectors"].pop()
                        self.bases[base.position.x]["gas_collectors0"].append(scv)
                        scv.right_click(self.bases[base.position.x]["refinery0"][0])

            if self.bases[base.position.x]["refinery1"] and len(self.bases[base.position.x]["gas_collectors1"]) < 3:
                for i in range(3-len(self.bases[base.position.x]["gas_collectors1"])):
                    if len(self.bases[base.position.x]["mineral_collectors"]) > 0:
                        scv = self.bases[base.position.x]["mineral_collectors"].pop()
                        self.bases[base.position.x]["gas_collectors1"].append(scv)
                        scv.right_click(self.bases[base.position.x]["refinery1"][0])


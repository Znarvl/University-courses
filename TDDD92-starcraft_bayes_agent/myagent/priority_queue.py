from library import *
import myagent.building as building
import myagent.military_recruit as military_recruit
from myagent.extra import has_addon
from myagent.eco import get_my_producers

# import myagent.chokepoints as chokepoints

class Priority_queue:
    def __init__(self):
        self.actions = []

    def isEmpty(self):
        return self.actions == []

    def enqueue(self, action):
        self.actions.append(action)

    def enqueueList(self, list):
        for i in list:
            self.actions.append(i)

    def prioenqueue(self, action):
        self.actions.insert(0, action)

    def dequeue(self):
        return self.actions.pop(0)

    def bottom(self):
        self.actions.insert(len(self.actions), self.actions[0])
        del self.actions[0]

    def peek(self):
        return self.actions[0]

    def size(self):
        return len(self.actions)

    def flush(self):
        return self.actions.clear()

    def list(self):
        return self.actions


def execute_econ_queue(self):
    if not self.econ_queue.isEmpty():
        action = self.econ_queue.peek()
        job_done = action(self)
        if job_done:
            self.econ_queue.dequeue()


def load_econ_queue(self): #Generalized build it uses before the naive bayes functions kicks in
    # self.econ_queue.enqueue(chokepoints.update_points_base)
    self.econ_queue.enqueue(building.build_barracks)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(building.build_orbital_command)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(building.build_factory)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(building.build_barracks)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(building.build_starport)
    self.econ_queue.enqueue(building.build_command_center)
    self.econ_queue.enqueue(building.build_factory_tech_lab)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(military_recruit.train_tank)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(building.build_engineering_bay)
    self.econ_queue.enqueue(military_recruit.train_tank)
    self.econ_queue.enqueue(military_recruit.train_medivacs)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(military_recruit.train_marines)
    self.econ_queue.enqueue(military_recruit.train_marines)















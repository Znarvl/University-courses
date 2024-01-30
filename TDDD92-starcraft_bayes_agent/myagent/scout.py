import random
from library import *


def worker_to_scout(self: IDABot, basePosX):
    self.bases[basePosX]["scouts"].append([self.bases[basePosX]["mineral_collectors"].pop(), False])


def maintain_scouting(self: IDABot):
    NUM_OF_MAX_SCOUTS = 1
    NUM_OF_MAX_SCOUT_BASES = 1
    numOfScoutBases = 0

    # Update bases to scout (enemy or unknown bases)
    for base in self.base_location_manager.base_locations:
        # Add base
        if base not in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF) and \
                [base, "not_scouted"] not in self.bases_to_scout and [base, "scouting"] not in self.bases_to_scout:
            self.bases_to_scout.append([base, "not_scouted"])
            print("Added base to scout!")
        # Remove base
        if base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
            if [base, "not_scouted"] in self.bases_to_scout:
                self.bases_to_scout.remove([base, "not_scouted"])
            if [base, "scouting"] in self.bases_to_scout:
                self.bases_to_scout.remove([base, "scouting"])

    # Create new scouts if needed
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        # create scouts list if it doesn't exits
        if "scouts" not in self.bases[base.position.x]:
            print("Creating Scout List!")
            self.bases[base.position.x]["scouts"] = []

        if len(self.bases[base.position.x]["mineral_collectors"]) > 0:
            if len(self.bases[base.position.x]["scouts"]) < NUM_OF_MAX_SCOUTS and numOfScoutBases < NUM_OF_MAX_SCOUT_BASES:
                # There are mineral workers to choose from and we need more scouts and we have enough scout bases active
                worker_to_scout(self, base.position.x)
                numOfScoutBases = numOfScoutBases + 1
                print("Scout unit joins the game...")

    # Update scout targeting
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        for scout in self.bases[base.position.x]["scouts"]:

            # Send new move orders to scouts or check if done.
            randInt = random.randint(0, len(self.bases_to_scout)-1)

            if self.bases_to_scout[randInt][1] == "not_scouted" and len(self.bases_to_scout) > 0 and scout[1] is False:
                scout[0].move(self.bases_to_scout[randInt][0].position)
                self.bases_to_scout[randInt][1] = "scouting"
                scout[1] = self.bases_to_scout[randInt][0]

            if type(scout[1]) is not bool:
                if 0 <= scout[1].get_ground_distance(scout[0].position) < 2:
                    scout[1] = False
                    self.bases_to_scout[randInt][1] = "not_scouted"

            """
            print("--------------")
            i = 0
            for scoutingbase in self.bases_to_scout:
                print(i, "-", scoutingbase[1])
                i = i + 1
            print("--------------")
            """


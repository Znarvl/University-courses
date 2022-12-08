from typing import Optional, Tuple, List
import numpy as np
import json
from library import *
import sc2reader

PATH = r"C:\Users\Simon\OneDrive\Dokument\StarcraftReplays"

#Filter bad stuff that gets extracted by the replay, we only want relevant data. Can be modified to append more terran objects
good_list = ["Barracks",
             "SCV",
             "Factory",
             "Reaper",
             "OrbitalCommand",
             "SupplyDepot",
             "SupplyDepotLowered",
             "Starport",
             "Cyclone",
             "Marine",
             "Marauder",
             "Raven",
             "SiegeTank",
             "SiegeTankSieged",
             "EngineeringBay",
             "Viking",
             "PlanetaryFortress",
             "Armory",
             "Medivac",
             "MissileTurret",
             "CommandCenter",
             "FusionCore",
             "Battlecruiser",
             "Banshee",
             "GhostAcademy",
             "Ghost",
             "Hellion",
             "Thor",
             "Liberator",
             ]


def formatReplay(replay):
    """
    Function from sc2.reader that just checks information of the current game being analysed
    """
    return """

{filename}
--------------------------------------------
SC2 Version {release_string}
{category} Game, {start_time}
{type} on {map_name}
Length: {game_length}

""".format(**replay.__dict__)


def formatTeams(replay):
    """
    Function form sc2.reader that checks what the teams
    """
    teams = list()
    for team in replay.teams:
        players = list()
        for player in team:
            players.append("({0}) {1}".format(player.pick_race[0], player.name))
        formattedPlayers = '\n         '.join(players)
        teams.append("Team {0}:  {1}".format(team.number, formattedPlayers))
    return '\n\n'.join(teams)


class Replay:
    def __init__(self):
        self.replays = sc2reader.load_replays(PATH, load_level=4)
        self.game = {}
        self.winners = []
        self.losers = []
        self.gameID = []

    def get_replay(self):
        """
        Play the replays to get build and unit order for both player 1 and 2 in seperate lists. Check who left game
        first (losers) and append losers to loser list and winner to winner list.
        """

        for replay in self.replays:
            print(formatReplay(replay))
            print(formatTeams(replay))
            player1 = []
            player2 = []
            for event in replay.events:
                if type(event) == sc2reader.events.game.PlayerLeaveEvent and replay.filename not in self.gameID:
                    self.gameID.append(replay.filename)  # Make sure that same replay ID does not append again
                    if event.player.pid == 1:
                        if not "Barracks" in player1 or not "Barracks" in player2: #sometimes barracks does not append. we do not want game without barracks!
                            print("No barracks in game = no fun remove!")
                        else:
                            self.losers.append(player1)
                            self.winners.append(player2)
                    elif event.player.pid == 2:
                        if not "Barracks" in player1 or not "Barracks" in player2:
                            print("No barracks in game = no fun remove!")
                        else:
                            self.winners.append(player1)
                            self.losers.append(player2)
                elif type(
                        event) == sc2reader.events.tracker.UnitInitEvent and event.unit.name in good_list and event.unit_controller.pid == 1 \
                        or type(
                    event) == sc2reader.events.tracker.UnitBornEvent and event.unit.is_army and event.unit.name in good_list and event.unit_controller.pid == 1 \
                        or type(
                    event) == sc2reader.events.tracker.UnitBornEvent and event.unit.is_worker and event.unit.name in good_list and event.unit_controller.pid == 1:
                    player1.append(event.unit.name)
                elif type(
                        event) == sc2reader.events.tracker.UnitInitEvent and event.unit.name in good_list and event.unit_controller.pid == 2 \
                        or type(
                    event) == sc2reader.events.tracker.UnitBornEvent and event.unit.name in good_list and event.unit.is_army and event.unit_controller.pid == 2 \
                        or type(
                    event) == sc2reader.events.tracker.UnitBornEvent and event.unit.name in good_list and event.unit.is_worker and event.unit_controller.pid == 2:
                    player2.append(event.unit.name)

        self.game = {
            "winners": self.winners,
            "losers": self.losers,
        }
        return self.game


if __name__ == "__main__":
    """
    Creates a JSON file from the winner and loser lists
    """
    trainer = Replay()
    games = trainer.get_replay()
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(games, f, ensure_ascii=False, indent=4)

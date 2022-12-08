import json
import math

from myagent import military_recruit, building


def change_dict(dictionary):
    """
    Because lowered supplydepot and sieged tanks has different id compared to non lowered supply depot and sieged tanks combine into one key instead of two
    """
    if "SupplyDepotLowered" in dictionary:
        value_supply = dictionary.get("SupplyDepotLowered")
        if value_supply is not None and "SupplyDepot" in dictionary:
            dictionary["SupplyDepot"] += value_supply
        else:
            dictionary["SupplyDepot"] = value_supply
        dictionary.pop("SupplyDepotLowered", None)
    if "SiegeTankSieged" in dictionary:
        value_tank = dictionary.get("SiegeTankSieged")
        if value_tank is not None and "SiegeTank" in dictionary:
            dictionary["SiegeTank"] += value_tank
        else:
            dictionary["SiegeTank"] = value_tank
        dictionary.pop("SiegeTankSieged", None)
    return dictionary


def round_values(dictionary):
    """
    To make it easier when there is a large quantity of something, round it to nearest five
    """
    key_to_be_rounded = ["Marine", "Viking", "SupplyDepot", "SiegeTank", "Marauder"]
    for key in dictionary:
        if key in key_to_be_rounded:
            dictionary[key] = 5 * round(dictionary[key] / 5)


def getWinnerLoserToDict():
    """
    Creates dictionaries of the JSON file for each game with corresponding winner and loser
    """
    listOfWinnerFreq = []
    listOfLoserFreq = []
    f = open(r'C:\Users\Simon\Documents\starcraft-ii-lab-agent-2020-sg-2-02\myagent\data.json')
    data = json.load(f)
    counterID= 0
    for item in data['winners']:
        winnerFreq = {}
        winnerFreq['id'] = counterID #Create ID in dictionary for specifict list in JSON
        counterID += 1
        for i in item:

            if i in winnerFreq:
                winnerFreq[i] += 1
            else:
                winnerFreq[i] = 1
        updatedWinFreq = change_dict(winnerFreq)
        round_values(updatedWinFreq)
        listOfWinnerFreq.append(updatedWinFreq)

    for item in data['losers']:
        loserFreq = {}
        for i in item:
            if i in loserFreq:
                loserFreq[i] += 1
            else:
                loserFreq[i] = 1
        updatedLosFreq = change_dict(loserFreq)
        round_values(updatedLosFreq)
        listOfLoserFreq.append(updatedLosFreq)
    return listOfWinnerFreq, listOfLoserFreq


def get_candidates(agentDict, enemyDict, winnerDict, loserDict):
    """
    Check all JSON dictionaries from winners and losers compared to what we know of the agent and enemy. If the agents or enemy dict is larger than correspoding JSON dictionary, ignore it. This is dynamic because
    we can loose buildings and units so removed dictionary could be relevant again.
    """
    candidatesWinner = []
    candidatesLoser = []
    for dictionary in winnerDict:
        is_bigger_winner = False
        for winnerKey, winnerValue in dictionary.items():
            if is_bigger_winner:
                break
            for agentKey, agentValue in agentDict.items():
                if agentKey == winnerKey:
                    if agentValue > winnerValue:
                        is_bigger_winner = True
                        if dictionary in candidatesWinner:
                            candidatesWinner.pop()
                        break
                    elif agentValue <= winnerValue and dictionary not in candidatesWinner:
                        is_bigger_winner = False
                        candidatesWinner.append(dictionary)

    for dictionary in loserDict:
        for loserKey, loserValue in dictionary.items():
            for enemyKey, enemyValue in enemyDict.items():
                if enemyKey == loserKey:
                    if enemyValue > loserValue:
                        if dictionary in candidatesLoser:
                            candidatesLoser.pop()
                        break
                    elif loserValue <= enemyValue and dictionary not in candidatesLoser:
                        candidatesLoser.append(dictionary)
    return candidatesWinner, candidatesLoser


def get_probability(winnerCandidates, loserCandidates):
    """ 
    Get probability for each state, we do this by dividing the state value with all values in the states.
    return with the dictionary with right key and its value.
    """
    winnerCandidatesProbability = []
    for dictionaries in winnerCandidates:
        dictionaryDenominator = sum(dictionaries.values()) - dictionaries.get('id')  # id shall not be in length of dict
        for key, value in dictionaries.items():
            if key != 'id':
                dictionaries[key] = ((value / dictionaryDenominator), value)
        winnerCandidatesProbability.append(dictionaries)

    loserCandidatesProbability = []
    for dictionaries in loserCandidates:
        dictionaryDenominator = sum(dictionaries.values())
        for key, value in dictionaries.items():
            dictionaries[key] = ((value / dictionaryDenominator), value)
        loserCandidatesProbability.append(dictionaries)
    return winnerCandidatesProbability, loserCandidatesProbability


def compare_probability(winnerProbList, loserProbList):
    """ 
    We use all the states probabilities by first getting the priori by how long the winner and loser list are and dividing.
    After getting the priori we multiply the priori with all the states by how many times they appear in the game. 
    """
    totalProbablilityWinner = []
    totalProbablilityLoser = []
    prioriWinner = len(winnerProbList) / (len(winnerProbList) + len(loserProbList))
    prioriLoser = len(loserProbList) / (len(loserProbList) + len(winnerProbList))
    for dictionary in winnerProbList:
        probability = prioriWinner
        for key, value in dictionary.items():
            if key != 'id':
                if value[1] != 0:
                    probability *= math.pow(dictionary[key][0], dictionary[key][1]) #probability of state times it appears in build order.

        totalProbablilityWinner.append((dictionary['id'], probability))

    for dictionary in loserProbList:
        probability = prioriLoser
        for key, value in dictionary.items():
            if value[1] != 0:
                probability *= math.pow(dictionary[key][0], dictionary[key][1]) #probability of state times it appears in build order.
        totalProbablilityLoser.append(probability)
    return totalProbablilityWinner, totalProbablilityLoser


def get_best_build_order(winnerList, loserList):
    """
    After getting the probablility of each dictionary/buildorder we compare the loser and winner list, if the winner > loser we append to the list with
    potential candidates. We then take the buildorder with best probablility. 
    """
    best_candidates_list = []
    for i in winnerList:
        for j in loserList:
            if i[1] > j and i[1] !=0:  # get biggest losers value
                best_candidates_list.append(i)
                break
    if len(best_candidates_list) != 0:
        return max(best_candidates_list, key=lambda x: x[1])
    else:
        print("Not enough obeservations or something went wrong")
        return (999,0)


def change_build_order(build_order, agentDict):
    """
    To not get duplicates when appending new build order, we look at the current state of the agent. We then iterate over the build order
    list and if it matches a state in game we look if we already got this element in game. If we have, subtract the value in dictionary and do nothing
    if the dictionary key value is 0 and we match element in list, append it to game because it is not a duplicate.
    
    """

    f = open(r'C:\Users\Simon\Documents\starcraft-ii-lab-agent-2020-sg-2-02\myagent\data.json')
    data = json.load(f)
    build_order_number = build_order[0] Get winning build order ID
    copy_dict = agentDict.copy()
    build_list = data["winners"][build_order_number] #Match the build order ID with the corresponding JSON list ID
    remove_units = [scv for scv in build_list if scv not in "SCV" or scv not in "OrbitalCommand" or scv not in "PlanetaryFortress"] # We remove elements we dont use, could be used in future to make more precise build order
    updated_with_tank = [build.replace('SiegeTankSieged', 'SiegeTank') for build in remove_units]
    removed_build_elements = []
    for build_order in updated_with_tank:
        for key, value in copy_dict.items():
            if key == build_order and copy_dict[key] > 0: #If we already have the value in game. Ignore appending to list and subtract one from the value
                copy_dict[key] -= 1
                break
            elif copy_dict[key] == 0: #We dont have any of these in game, add to list.
                removed_build_elements.append(build_order)
                break
    return removed_build_elements, build_order_number

def make_build_order_to_functions(build_order):
    """
    When having the complete buildorder, we must redo the string to actual fuctioncalls. We do this by looking at the list and if it matches a state in game,
    we redo this to a funcion and append it to the list.
    """
    function_order = []
    for i in build_order:
        if i == "Marine":
            i = military_recruit.train_marines
            function_order.append(i)

        if i == "Marauder":
            i = military_recruit.train_marauders
            function_order.append(i)

        if i == "Reaper":
            i = military_recruit.train_reapers
            function_order.append(i)
            
        if i == "Ghost":
            i = military_recruit.train_ghosts
            function_order.append(i)
        if i == "Hellion":
            i = military_recruit.train_hellion
            function_order.append(i)
        if i == "SiegeTank":
            i = military_recruit.train_tank
            function_order.append(i)
            
        if i == "Cyclone":
            i = military_recruit.train_cyclone
            
        if i == "Thor":
            i = military_recruit.train_thor
            function_order.append(i)
        if i == "Viking":
            i = military_recruit.train_vikings
            function_order.append(i)
            
        if i == "Medivac":
            i = military_recruit.train_medivacs
            function_order.append(i)
            
        if i == "Liberator":
            i = military_recruit.train_liberators
            function_order.append(i)

        if i == "Raven":
            i = military_recruit.train_ravens
            function_order.append(i)

        if i == "Banshee":
            i = military_recruit.train_banshees
            function_order.append(i)

        if i == "Battlecruiser":
            i = military_recruit.train_battlecruiser
            function_order.append(i)

        if i == "CommandCenter":
            i = building.build_command_center
            function_order.append(i)

        if i == "PlanetaryFortress":
            i = building.build_planetary_fortress
            function_order.append(i)
            
        if i == "OrbitalCommand":
            i = building.build_orbital_command
            function_order.append(i)

        if i == "Barracks":
            i = building.build_barracks
            function_order.append(i)

        if i == "EngineeringBay":
            i = building.build_engineering_bay
            function_order.append(i)
        
        if i == "MissleTurret":
            i = building.build_missle_turret
            function_order.append(i)

        if i == "Factory":
            i = building.build_factory
            function_order.append(i)
        
        if i == "GhostAcademy":
            i = building.build_ghost_academy
            function_order.append(i)
        
        if i == "Starport":
            i = building.build_starport
            function_order.append(i)
        if i == "Armory":
            i = building.build_armory
            function_order.append(i)

        if i == "FusionCore":
            i = building.build_fusion_core
            function_order.append(i)
    return function_order





def naive_bayes(agentDict, enemyDict):
    """
    The main function of naive bayes, it take in all other functions to find the best build order to append in game. To do this we get the values of           thestates from the agent and enemy in game. We need observations to make predictions so the function will not analyse before it has seen atleast 15 key values of the enemy.
    """

    winnerDict, loserDict = getWinnerLoserToDict()
    if sum(enemyDict.values()) > 15:
        winnerCandidates, loserCandidates = get_candidates(agentDict, enemyDict, winnerDict, loserDict)
        winnerProbList, loserProbList = get_probability(winnerCandidates, loserCandidates)
        totalProbListWinner, totalProbListLoser = compare_probability(winnerProbList, loserProbList)
        build_order_number = get_best_build_order(totalProbListWinner, totalProbListLoser)
        if build_order_number == 999: # If it cant find any good candidates the list will be empty and set to 999
            print("Something went terrible wrong")
            return "404", "404"
        build_order, build_number = change_build_order(build_order_number, agentDict)
        build_order_to_function = make_build_order_to_functions(build_order)
        return build_order_to_function, build_number


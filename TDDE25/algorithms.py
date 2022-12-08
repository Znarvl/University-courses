import math
import sys
from heapq import heapify, heappop, heappush
from collections import defaultdict
from decimal import Decimal
from operator import add, sub

def length_haversine(p1, p2):
    lat1 = p1.lat
    lng1 = p1.lng
    lat2 = p2.lat
    lng2 = p2.lng
    lat1, lng1, lat2, lng2 = map(math.radians, [lat1, lng1, lat2, lng2])
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    return 6372797.560856 * c # return the distance in meters

def get_closest_node_id(nodes, source_node):
    """ Search through all nodes and return the id of the node
    that is closest to 'source_node'. """
    min_distance = float("inf")
    count = 0
    for node in nodes.values():
        distance = length_haversine(node, source_node)
        if distance < min_distance:
            min_distance = distance
            closest_node = node
        count += 1
    print("Closest node count:", count)
    return closest_node.id

def get_closest_node_id_grid_search(grid, source_node):
    """
    Search through nodes using grid search and return the id of the node
    that is closest to 'source_node'.
    """
    min_distance = float("inf")
    source_coords = source_node.rounded_coords()
    selected_coords = [source_coords]
    delta = Decimal('0')

    count = 0
    while min_distance == float("inf"):
        # start with the immediate area around the source_node.
        # If there are no nodes in that area, expand the area by +-0.001
        # until the closest node is found
        selected_area = []
        for coords in selected_coords:
            # Runs the add/subtract operation on both tuple values
            plus_delta = grid[tuple(map(add, coords, (delta, delta)))]
            selected_area.append(plus_delta)
            minus_delta = grid[tuple(map(sub, coords, (delta, delta)))]
            selected_area.append(minus_delta)
        if sum(len(x) for x in selected_area) == 0:
            print("No nearby nodes found: expanding area.")
            delta += Decimal('0.001')
            continue

        for area in selected_area:
            for node in area:
                distance = length_haversine(node, source_node)
                if distance < min_distance:
                    min_distance = distance
                    closest_node = node
                count += 1
    print("Grid search count:", count)
    return closest_node.id


class HeapItem_d:
    """ HeapItem specifically used for Dijkstra's algorithm """
    def __init__(self, node_id, distance, path):
        self.node_id = node_id
        self.distance = distance
        self.path = path

    def __lt__(self, other_heap_item):
        return self.distance < other_heap_item.distance

def dijkstra(nodes, source_id, target_id):
    """ Return the shortest path using Dijkstra's algortihm. """
    queue = []
    # insert our source node into the queue with a distance of 0
    heappush(queue, HeapItem_d(source_id, 0, [source_id]))
    visited = set()
    shortest_distances = defaultdict(lambda: float("inf"))
    shortest_path = (float("inf"), [])

    # while queue is not empty:
    while queue:
        # remove the node with the shortest distance from the queue
        item = heappop(queue)
        item_node = nodes[item.node_id]
        # if node is our target:
        # save the path to this node as our shortest_path
        # save the distance as the shortest_distance
        # stop looping
        if item.node_id == target_id:
            shortest_path = (item.distance, item.path)
            break

        # if node has not been visited before:
        if item.node_id not in visited:
            # add the node to visited nodes
            visited.add(item.node_id)
            # for every neighbor to the node:
            for neighbor_id in item_node.neighbors:
                # makes sure that neighbor is accessible by the chosen
                # mode of transporation.
                if neighbor_id not in nodes.keys():
                    continue
                neighbor_node = nodes[neighbor_id]
                neighbor_weight = length_haversine(neighbor_node, item_node)
                distance = neighbor_weight + item.distance
                # if total distance to neighbor node is less than the prior shortest distance to the neighbor node:
                # update the total shortest distance to this neighbor node
                # add it and its distance to the queue
                # set the path to this node
                if distance < shortest_distances[neighbor_id]:
                    neighbor_path = item.path + [neighbor_id]
                    shortest_distances[neighbor_id] = distance
                    neighbor_node.distance = distance
                    heappush(queue, HeapItem_d(neighbor_id,
                        distance, neighbor_path))
    return shortest_path


class HeapItem_a:
    """ Used to keep track of and prioritize nodes in the pathfinding algorithms """
    def __init__(self, node_id, path_distance, distance_left, path):
        self.node_id = node_id
        self.path_distance = path_distance
        self.distance_left = distance_left
        self.path = path

    def __lt__(self, other_heap_item):
        return self.distance_left + self.path_distance < other_heap_item.distance_left + other_heap_item.path_distance

def a_star(nodes, source_id, target_id):
    """
    Return the shortest path using the A* algortihm.
    The difference is that HeapItems are ordered not only by their path distance
    but also the optimal distance left to the target node.
    """
    queue = []
    target_node = nodes[target_id]
    total_distance = length_haversine(nodes[source_id], target_node)
    heappush(queue, HeapItem_a(source_id, 0, total_distance, [source_id]))
    visited = set()
    shortest_distances = defaultdict(lambda: float("inf"))
    shortest_path = (float("inf"), [])

    while queue:
        item = heappop(queue)
        item_node = nodes[item.node_id]
        if item.node_id == target_id:
            shortest_path = (item.path_distance, item.path)
            break

        if item.node_id not in visited:
            visited.add(item.node_id)
            for neighbor_id in item_node.neighbors:
                if neighbor_id not in nodes.keys():
                    continue
                neighbor_node = nodes[neighbor_id]
                neighbor_weight = length_haversine(neighbor_node,
                    item_node)
                path_distance = neighbor_weight + item.path_distance
                distance_left = length_haversine(item_node, target_node)
                if path_distance < shortest_distances[neighbor_id]:
                    neighbor_path = item.path + [neighbor_id]
                    shortest_distances[neighbor_id] = path_distance
                    neighbor_node.path_distance = path_distance
                    heappush(queue, HeapItem_a(neighbor_id,
                        path_distance, distance_left, neighbor_path))
    return shortest_path
from osm_parser import get_default_parser
from collections import defaultdict
from decimal import Decimal

# list of suitable tags for cars
tag_lst = ['motorway', 'trunk', 'primary', 'secondary', 'tertiary',
    'unclassified', 'residential', 'service', 'motorway_link', 'trunk_link',
    'primary_link', 'secondary_link', 'tertiary_link', 'living_street']

# list of suitable tags for bikes
bike_lst = ['lane', 'opposite', 'opposite_lane', 'track', 'opposite_track',
    'share_busway', 'opposite_share_busway', 'shared_lane', 'lane', 'footway', 'cycleway'
    , 'living_street', 'path', 'raceway', 'track', 'pedestrian', 'living_street',
    'residential', 'teritary', 'secondary_link']

class Node:
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = float(lat)
        self.lng = float(lng)
        self.neighbors = []

    def rounded_coords(self):
        """
        Return tuple of coordinates rounded to 3 decimals.
        Using Decimal objects to ensure floating point precision in grid
        search.
        """
        lat = Decimal(str(self.lat)).quantize(Decimal('.001'))
        lng = Decimal(str(self.lng)).quantize(Decimal('.001'))
        return (lat, lng)

def extract_osm_nodes(f_name):
    global parser
    parser = get_default_parser(f_name)
    nodes = dict()

    for node in parser.iter_nodes():
        nodes[node['id']] = Node(node['id'], node['lat'], node['lon'])

    return nodes

def add_neighbors(nodes):
    """
    Bundles nodes into two dictionaries used for cars and bikes,
    respectively.
    """
    nodes_car = {}
    nodes_bike = {}
    for way in parser.iter_ways():
        if has_correct_tag_car(way):
            road = way['road']
            length = len(road)
            for i in range(length - 1):
                node_id = road[i]
                neigh_id = road[i + 1]
                nodes_car[node_id] = nodes[node_id]
                nodes_car[neigh_id] = nodes[neigh_id]
                nodes_car[node_id].neighbors.append(neigh_id)
                nodes_car[neigh_id].neighbors.append(node_id)
        if has_correct_tag_bike(way):
            road = way['road']
            length = len(road)
            for i in range(length - 1):
                node_id = road[i]
                neigh_id = road[i + 1]
                nodes_bike[node_id] = nodes[node_id]
                nodes_bike[neigh_id] = nodes[neigh_id]
                nodes_bike[node_id].neighbors.append(neigh_id)
                nodes_bike[neigh_id].neighbors.append(node_id)

    return (nodes_car, nodes_bike)

def has_correct_tag_car(way):
    """ Checks if way is accessible by car """
    tags = way['tags']
    if 'highway' in tags:
        if tags['highway'] in tag_lst:
            return True
    return False

def has_correct_tag_bike(way):
    """ Checks if way is accessible by bike """
    tags = way['tags']
    if 'cycleway' in tags:
        if tags['cycleway'] in bike_lst:
            return True
    if 'highway' in tags:
        if tags['highway'] in bike_lst:
            return True
    return False

def process_nodes(nodes):
    """
    Removes nodes without neighbors and adds them to _nodes
    Also creates a grid which bundles nearby nodes together for quicker
    searching.
    """
    _nodes = {}
    grid = defaultdict(list)

    for node in nodes.values():
        if node.neighbors:
            _nodes[node.id] = node
            grid[node.rounded_coords()].append(node)

    return (_nodes, grid)
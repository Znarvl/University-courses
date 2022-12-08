from lib import *
from time import clock
import json
from store import Node, extract_osm_nodes, add_neighbors, process_nodes
from algorithms import get_closest_node_id, get_closest_node_id_grid_search, a_star, dijkstra
import hashlib

logged_in = False
logged_in_user = None
del logged_in_user


@get('/')
def index():
    return read_html('templates/index.html')

@get('/data/favicon.ico')
def favicon():
    """reads favicon image file as bytes and saves it as variable iconbytes"""
    with open("data/favicon.ico", mode='rb') as binary_file:
        iconbytes = binary_file.read()
    return iconbytes


@post('/login')
def login(body):
    """Gets username and password input from the body and logs the user in if
    corresponding data is found in the .json database
    Uses sha-2 with 512 bit hash do encrypt password. Hexdigest returns a
    string instead of bytes which is easier to store in Json and read.
    Saves the username and logged-in-status in a global variable for other user
    functionality"""
    global logged_in, logged_in_user
    body = json.loads(body)
    username_input = body['username']
    password_input = hashlib.sha512(body['password'].encode()).hexdigest()
    with open('users.json') as user_db:
        users = json.load(user_db)
        if username_input in users:
            password = users[username_input]['password']
        if username_input in users and password == password_input:
            response = "success"
            logged_in = True
            logged_in_user = username_input
        else:
            response = "user not found"
    return json.dumps(response)


@post('/register')
def register(body):
    """registers and logs in a user if the username doesn't already exist in
    users.json, encrypts the password and add  and last bike
    /car path in a dictionary for the user"""
    global logged_in, logged_in_user
    body =  json.loads(body)
    username = body['username']
    password = body['password']
    with open('users.json') as user_db:
        users = json.load(user_db)
        if username not in users:
            password = hashlib.sha512(password.encode()).hexdigest()
            users[username] = {'password':"", 'last_car_path':[], 'last_bike_path':[]}
            users[username]['password'] = password
            with open('users.json', 'w') as json_file:
                 json.dump(users, json_file,  sort_keys=True, indent=4, separators=(',', ': '))#
                 #arguments after json_file are for pretty print in the database
            response ="success"
            logged_in = True
            logged_in_user = username
        else:
            response = "user exists"
    return json.dumps(response)


@post('/logout')
def logout(body):
    """changes login status and deletes the username variable """
    global logged_in, logged_in_user
    body = json.loads(body)
    if logged_in == True:
        response = "success"
        logged_in = False
        del logged_in_user
    else:
        response = "error"
    return json.dumps(response)


@post('/shortest-path')
def shortest_path(body, trans_mode):
    if trans_mode == "car":
        grid = car_grid
        nodes = car_nodes
    elif trans_mode == "bike":
        grid = bike_grid
        nodes = bike_nodes

    body = json.loads(body)

    try:
        lat1 = float(body['lat1'])
        lng1 = float(body['lng1'])
        lat2 = float(body['lat2'])
        lng2 = float(body['lng2'])
    except ValueError:
        print("ValueError: Could not parse lat/lng")

    # Uncomment to test closest node performance
    # start = clock()
    # source_id = get_closest_node_id(nodes, Node('-1', lat1, lng1))
    # target_id = get_closest_node_id(nodes, Node('-1', lat2, lng2))
    # end = clock()
    # print("Closest node speed:", end-start)

    start = clock()
    source_id = get_closest_node_id_grid_search(grid, Node('-1', lat1, lng1))
    target_id = get_closest_node_id_grid_search(grid, Node('-1', lat2, lng2))
    end = clock()
    print("Grid search speed:", end-start)

    # uncomment to test Dijkstra performance
    # start = clock()
    # path = dijkstra(nodes, source_id, target_id)
    # end = clock()
    # print("Dijkstra speed:", end-start)

    start = clock()
    path = a_star(nodes, source_id, target_id)
    end = clock()
    print("A* speed:", end-start)

    if path == (float("inf"), []):
        print("No path found.")
        return

    path_nodes = path[1]
    print("source_id:", source_id)
    print("target_id:", target_id)
    print(path)
    for i in range(len(path_nodes)):
        path_nodes[i] = (nodes[path_nodes[i]].lat,
            nodes[path_nodes[i]].lng)
    response = {'path': path_nodes, 'start':[lat1,lng1], 'end':[lat2,lng2]}#
    #'end' and 'start' is the markers coordinates, saved for user options

    if logged_in:
        with open('users.json') as json_file:
            users = json.load(json_file)

            if trans_mode == "car":
                users[logged_in_user]['last_car_path'] =  response

            elif trans_mode == "bike":
                users[logged_in_user]['last_bike_path'] = response

            with open('users.json', 'w') as json_file:
                 json.dump(users, json_file,  sort_keys=True, indent=4, separators=(',', ': '))

    return json.dumps(response)

@post('/shortest-car-path')
def shortest_car_path(body):
    """ Runs when user presses 'Find car path' """
    return shortest_path(body, "car")

@post('/shortest-bike-path')
def shortest_bike_path(body):
    """ Runs when user presses 'Find bike path' """
    return shortest_path(body, "bike")

@post('/last-car-path')
def last_car_path(body):
    """returns the car path last requested by the logged in user"""
    global logged_in, logged_in_user
    body =  json.loads(body)
    with open('users.json') as json_file:
        users = json.load(json_file)
        if logged_in:
            if 'path' in users[logged_in_user]['last_car_path']: #key for path
                #is always 'path'
                response = users[logged_in_user]['last_car_path']
            else:
                response = "no last car path"
    return json.dumps(response)


@post('/last-bike-path')
def last_bike_path(body):
    """returns the bike path last requested by the logged in user if there is one"""
    global logged_in, logged_in_user
    body =  json.loads(body)
    with open('users.json') as json_file:
        users = json.load(json_file)
        if logged_in:
            if 'path' in users[logged_in_user]['last_bike_path']:
                response = users[logged_in_user]['last_bike_path']
            else:
                response = "no last bike path"
    return json.dumps(response)

if __name__ == "__main__":
    nodes = extract_osm_nodes('map')
    print("nodes incl. singles: ", len(nodes))
    car_nodes, bike_nodes = add_neighbors(nodes)
    car_nodes, car_grid = process_nodes(car_nodes)
    bike_nodes, bike_grid = process_nodes(bike_nodes)
    print("Car nodes excl. singles: ", len(car_nodes))
    print("Bike nodes excl. singles: ", len(bike_nodes))
    run_server()

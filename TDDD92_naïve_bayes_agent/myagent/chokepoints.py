import queue
from myagent.extra import find_start_location
from library import *


def flood_fill(self):
    """The FloodFill algorithm to find places on the map that are walkable"""
    q = queue.Queue()
    q.put((100, 100))
    while not q.empty():
        node = q.get()
        if self.map_tools.is_walkable(node[0], node[1]):
            self.walkable_points.append(node)
            node1 = (node[0] - 1, node[1])
            node2 = (node[0], node[1] + 1)
            node3 = (node[0] + 1, node[1])
            node4 = (node[0], node[1] - 1)
            if node1 not in self.chokepoint_tried:
                q.put(node1)
                self.chokepoint_tried.append(node1)
            if node2 not in self.chokepoint_tried:
                q.put(node2)
                self.chokepoint_tried.append(node2)
            if node3 not in self.chokepoint_tried:
                q.put(node3)
                self.chokepoint_tried.append(node3)
            if node4 not in self.chokepoint_tried:
                q.put(node4)
                self.chokepoint_tried.append(node4)


def to_file(self):
    """Makes a new map in a text file with data from FloodFill algorithm"""
    flood_fill(self)
    outF = open("floodfill.txt", "w")
    self.chokepoint_tried.sort()
    for x in range(0, 160):
        for y in range(200, 0, -1):
            if (x, y) in self.walkable_points:
                outF.write("*")
                self.map[x][y] = "*"
            elif (x, y) in self.chokepoint_tried:
                outF.write("-")
                self.map[x][y] = "-"
            else:
                outF.write("X")
        outF.write(str(y) + "\t")
        outF.write(str(x) + "\n")
    outF.close()
    find_choke_point(self)


def find_choke_point(self):
    """Algorithm to find the chokepoints. Iterates 5 times to find points on depth of five"""
    for i in range(5):
        for x in range(0, 160):
            for y in range(200, 0, -1):
                if self.map[x][y] is "*":
                    # Add points that are walkable but beside a point that are not walkable
                    if self.map[x+1][y] is "-" or self.map[x+1][y] is "X":
                        self.map[x][y] = 0
                    if self.map[x-1][y] is "-" or self.map[x-1][y] is "X":
                        self.map[x][y] = 0
                    if self.map[x][y+1] is "-" or self.map[x][y+1] is "X":
                        self.map[x][y] = 0
                    if self.map[x][y-1] is "-" or self.map[x][y-1] is "X":
                        self.map[x][y] = 0
                    if self.map[x+1][y] is i-1 or self.map[x-1][y] is i-1 or self.map[x][y+1] is i-1 or self.map[x][y-1] is i-1:
                        self.map[x][y] = i
        for x in range(0, 160):
            for y in range(200, 0, -1):
                # Find choke points depending on the x coordinate
                if self.map[x][y] is i and self.map[x+1][y] is i-1 and self.map[x-1][y] is i-1 and \
                        self.map[x][y+5] is "*" and self.map[x][y-5] is "*" and self.map[x][y+1] is not "*" and self.map[x][y-1] is not "*":
                    self.chokepoint.append((x, y))
                if self.map[x][y] is i and self.map[x+1][y] is i and self.map[x-1][y] is i-1 and \
                        self.map[x][y+5] is "*" and self.map[x][y-5] is "*" and self.map[x][y+1] is not "*" and self.map[x][y-1] is not "*":
                    self.chokepoint.append((x, y))
                if self.map[x][y] is i and self.map[x+1][y] is i-1 and self.map[x-1][y] is i and \
                        self.map[x][y+5] is "*" and self.map[x][y-5] is "*" and self.map[x][y+1] is not "*" and self.map[x][y-1] is not "*":
                    self.chokepoint.append((x, y))
                # Find choke points depending on the y coordinate
                if self.map[x][y] is i and self.map[x][y+1] is i - 1 and self.map[x][y-1] is i - 1 and \
                        self.map[x+5][y] is "*" and self.map[x-5][y] is "*" and self.map[x+1][y] is not "*" and self.map[x-1][y] is not "*":
                    self.chokepoint.append((x, y))
                if self.map[x][y] is i and self.map[x][y+1] is i and self.map[x][y-1] is i - 1 and \
                        self.map[x+5][y] is "*" and self.map[x-5][y] is "*" and self.map[x+1][y] is not "*" and self.map[x-1][y] is not "*":
                    self.chokepoint.append((x, y))
                if self.map[x][y] is i and self.map[x][y+1] is i - 1 and self.map[x][y-1] is i and \
                        self.map[x+5][y] is "*" and self.map[x-5][y] is "*" and self.map[x+1][y] is not "*" and self.map[x-1][y] is not "*":
                    self.chokepoint.append((x, y))
    self.chokepoint.sort()
    """for point in self.chokepoint:
        self.map[point[0]][point[1]] = "T"
    out = open("floodfill2.txt", "w")
    for x in range(0, 160):
        for y in range(200, 0, -1):
            out.write(str(self.map[x][y]))
        out.write("\n")
    out.close()"""


def update_points_base(self):
    """Travers the list of choke points if the base is in SE"""
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        # base in SE, need to travers the chokepointlist
        if self.map_tools.get_ground_distance(base.position, Point2D(self.chokepoint[-1][0], self.chokepoint[-1][1])) < \
                self.map_tools.get_ground_distance(base.position, Point2D(self.chokepoint[0][0], self.chokepoint[0][1])):
            temp = []
            for i in range(len(self.chokepoint)-1, 0, -1):
                temp.append(self.chokepoint[i])
            self.chokepoint = temp
    limit_number_of_chokepoints(self)
    return True


def limit_number_of_chokepoints(self):
    """Limit the number of choke points to only get the points near the base"""
    add = []
    for base in self.base_location_manager.get_occupied_base_locations(PLAYER_SELF):
        for position in self.chokepoint:
            distans = self.map_tools.get_ground_distance(base.position, Point2D(position[0], position[1]))
            if distans < 100:
                add.append(position)
    self.chokepoint = add






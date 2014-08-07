#!/usr/bin/env python
# szqh97@163.com
#2014-07-31 15:09:25

import Queue

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __cmp__(self, oth):
        return cmp(self.x , oth.x ) and cmp(self.y, oth.y)
    def __hash__(self):
        return  hash(str(self.x) + "," + str(self.y))

def get_direction(p1, p2):
    if p2.x - p1.x == 1 and p2.y == p1.y:
        print 'R'
        return 'R'
    if p2.y - p1.y == 1 and p2.x == p1.x:
        print 'D'
        return 'D'
def print_path(path):
    s_path = ""
    for i in xrange(len(path)-1):
        s_path += get_direction(path[i], path[i+1])
    return path



class Maze(object):
    def __init__(self, strmazevars):

        self.frontier = Queue.Queue()
        self.frontier.put(Point(0,0))
        self.come_from = {}
        self.come_from[Point(0,0)] = True


        self.graph = []
        self.maxsteps = -1
        self.minsteps = -1
        maze_vars = strmazevars.split('&')

        for s in maze_vars:
            if s.startswith("FVterrainString="):
                strMaze = s[len("FVterrainString="):]
            if s.startswith("FVinsMin="):
                self.minsteps = int(s[len("FVinsMin="):])
            if s.startswith("FVinsMax="):
                self.maxsteps = int(s[len("FVinsMax="):])
            if s.startswith("FVboardX="):
                self.xboard = int(s[len("FVboardX="):])
            if s.startswith("FVboardY="):
                self.yboard = int(s[len("FVboardY="):])
            if s.startswith("FVlevel="):
                self.level= int(s[len("FVlevel="):])

        for i in range(self.yboard):
            s = strMaze[0 : self.xboard]
            strMaze = strMaze[self.xboard:]
            if len(s) == self.xboard:
                self.graph.append(s)

        if len(self.graph) != self.yboard:
            print "error, construct maze map failed!"
            sys.exit(-1)

    def get_neighbours(self, point):
        neighbours = []
        # get right neighbour
        tmpx = point.x + 1
        tmpy = point.y
        if tmpx < self.xboard and tmpy < self.yboard and self.graph[tmpy][tmpx] == '.':
            neighbours.append(Point(tmpx, tmpy))

        # get bottom neighbour
        tmpx = point.x 
        tmpy = point.y + 1
        if tmpx < self.xboard and tmpy < self.yboard and self.graph[tmpy][tmpx] == '.':
            neighbours.append(Point(tmpx, tmpy))
        return neighbours

    def get_come_from_list(self):
        while not self.frontier.empty():
            print self.frontier.qsize(), len(self.come_from)
            current = self.frontier.get()
            for next in self.get_neighbours(current):
                if not self.come_from.has_key(next):
                    self.frontier.put(next)
                    self.come_from[next] = current
    
    def get_endpoints(self):
        """ get available end points"""
        self.end_points=[]
        for y in xrange(self.yboard):
            x = self.xboard - 1
            if self.graph[y][x] == '.' :
                self.end_points.append(Point(x, y))
        for x in xrange(self.xboard - 1):
            y = self.yboard - 1
            if self.graph[y][x] == '.':
                self.end_points.append(Point(x,y))
 
    def get_all_path(self):
        self.get_come_from_list()
        self.get_endpoints()
       
        print len(self.end_points)
        for p in self.end_points:
            print "(", str(p.x) + ", " + str(p.y) + "), "

        start = Point(0, 0)
        for p in self.end_points:
            x = p.x
            y = p.y
            if p.x == self.xboard - 1:
                x += 1
            if p.y == self.yboard - 1:
                y += 1
            path = [Point(x, y)]


            current = p
            path.append(current)
            if self.come_from.has_key(p):
                while current != start:
                    current = self.come_from[current]
                    path.append(current)
                if current == start:
                    path.append(start)
                    path.reverse()
                    print print_path(path)
                    #print "path len ", len(path), path
                    for p in path:
                        print "(", str(p.x) + ", " + str(p.y) + "), "

    


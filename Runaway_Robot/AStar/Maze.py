#!/usr/bin/env python
# szqh97@163.com
#2014-07-31 15:09:25

import Queue
import time

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __cmp__(self, oth):
        return cmp(self.x , oth.x ) and cmp(self.y, oth.y)
    def __hash__(self):
        return  hash(str(self.x) + "," + str(self.y))

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
    
    def get_all_path(self):
        end_points = []
        for y in xrange(self.yboard):
            x = self.xboard - 1
            if self.graph[y][x] == '.':
                end_points.append(Point(x, y))
        for x in xrange(self.xboard - 1):
            y = self.yboard - 1
            if self.graph[y][x] == '.':
                end_points.append(Point(x,y))
        
        print len(end_points)
        start = Point(0, 0)
        for p in end_points:
            current = p
            path = [current]
            if self.come_from.has_key(p):
                while current != start:
                    current = self.come_from[current]
                    path.append(current)
                if current == start:
                    print "path len ", len(path), path
                    for p in path:
                        print "(", str(p.x) + ", " + str(p.y) + "), "



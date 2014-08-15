#!/usr/bin/env python
# szqh97@163.com
#2014-07-31 15:09:25

import Queue
import collections

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __cmp__(self, oth):
        return cmp((self.x, self.y), (oth.x, oth.y))

    def __hash__(self):
        return hash(str(self.x) + ',' + str(self.y))

    def __str__(self):
        return '(%d,%d)' % (self.x, self.y)


def get_direction(p1, p2):
    if p2.x - p1.x == 1 and p2.y == p1.y:
        return 'R'
    if p2.y - p1.y == 1 and p2.x == p1.x:
        return 'D'


def print_path(path):
    s_path = ''
    for i in xrange(len(path) - 1):
        s_path += get_direction(path[i], path[i + 1])

    return s_path


class Maze(object):

    def __init__(self, strmazevars):
        self.frontier = Queue.Queue()
        self.frontier.put(Point(0, 0))
        self.come_from = {}
        self.come_from[Point(0, 0)] = True
        self.graph = []
        self.maxsteps = -1
        self.minsteps = -1
        maze_vars = strmazevars.split('&')
        for s in maze_vars:
            if s.startswith('FVterrainString='):
                strMaze = s[len('FVterrainString='):]
            if s.startswith('FVinsMin='):
                self.minsteps = int(s[len('FVinsMin='):])
            if s.startswith('FVinsMax='):
                self.maxsteps = int(s[len('FVinsMax='):])
            if s.startswith('FVboardX='):
                self.xboard = int(s[len('FVboardX='):])
            if s.startswith('FVboardY='):
                self.yboard = int(s[len('FVboardY='):])
            if s.startswith('FVlevel='):
                self.level = int(s[len('FVlevel='):])

        for i in range(self.yboard):
            s = strMaze[0:self.xboard]
            strMaze = strMaze[self.xboard:]
            if len(s) == self.xboard:
                self.graph.append(s)

        if len(self.graph) != self.yboard:
            print 'error, construct maze map failed!'
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
        """
          come_from is like ;
          { A:[B, C],
            B:[C],
            C:[D,E]
          }
        """
        while not self.frontier.empty():
            current = self.frontier.get()
            next_steps = [ p for p in self.get_neighbours(current) ]
            if next_steps:
                self.come_from[current] = next_steps
            for next in next_steps:
                self.frontier.put(next)

        for p in self.come_from:
            print '(', p.x, ',', p.y, ') : ['
            for pp in self.come_from[p]:
                print ' (', pp.x, ', ', pp.y, '),'

            print ']'

    def get_endpoints(self):
        """ get available end points"""
        self.end_points = []
        for y in xrange(self.yboard):
            x = self.xboard - 1
            if self.graph[y][x] == '.':
                self.end_points.append(Point(x, y))

        for x in xrange(self.xboard - 1):
            y = self.yboard - 1
            if self.graph[y][x] == '.':
                self.end_points.append(Point(x, y))

    def find_all_path1end(self, start, end_point, path = []):
        path = path + [start]
        if start == end_point:
            return [path]
        if not self.come_from.has_key(start):
            return []
        paths = []
        for node in self.come_from[start]:
            if node not in path:
                newpaths = self.find_all_path1end(node, end_point, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths

    def get_all_path(self):
        self.get_come_from_list()
        self.get_endpoints()
        start = Point(0, 0)
        all_paths = []
        for end in self.end_points:
            print str(end)
            paths = self.find_all_path1end(start, end)
            print len(paths)
            if end.x == self.xboard - 1:
                all_paths = all_paths + [ path + [Point(end.x + 1, end.y)] for path in paths ]
            if end.y == self.yboard - 1:
                all_paths = all_paths + [ path + [Point(end.x, end.y + 1)] for path in paths ]

        str_all_paths = [ print_path(path) for path in all_paths ]
        return str_all_paths

    def get_fist_available_path(self):
        step = ''
        for path in self.get_all_path():
            for steplen in xrange(self.minsteps, self.maxsteps + 1):
                step = path[0:steplen]
                cnt = len(path) / steplen + 1
                expend_path = step * cnt
                if expend_path.startswith(path):
                    return step


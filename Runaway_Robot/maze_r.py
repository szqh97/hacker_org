#!/usr/bin/env python

import sys
from arrange import arrange
FlashVars = "FVterrainString=..X..X.....XX..XX.X....XX..........X&FVinsMax=4&FVinsMin=3&FVboardX=6&FVboardY=6&FVlevel=6"

grid = []
def hack_maze_path():
    maze = lambda: None
    maze.lmap = []
    lMaze = FlashVars.split('&')
    for s in lMaze:
        if s.startswith("FVterrainString="):
            strMaze = s[len("FVterrainString="):]
        if s.startswith("FVinsMin="):
            maze.iMinSteps = int(s[len("FVinsMin="):])
        if s.startswith("FVinsMax="):
            maze.iMaxSteps = int(s[len("FVinsMax="):])
        if s.startswith("FVboardX="):
            maze.iXBoard = int(s[len("FVboardX="):])
        if s.startswith("FVboardY="):
            maze.iYBoard = int(s[len("FVboardY="):])
        if s.startswith("FVlevel="):
            maze.iLevel= int(s[len("FVlevel="):])

    for i in range(maze.iYBoard):
        s = strMaze[0 : maze.iXBoard]
        s += 'E'
        strMaze = strMaze[maze.iXBoard:]
        if len(s) == maze.iXBoard + 1:
            maze.lmap.append(list(s))
    strlast = 'E' * (maze.iYBoard + 1)
    maze.lmap.append(list(strlast))
    if len(maze.lmap) != maze.iYBoard + 1:
        print "error, construct maze map failed!"
        sys.exit(-1)

    print "strMaze :" + strMaze + ", maze.iMaxSteps: " + str(maze.iMaxSteps) + \
        ", maze.iMinSteps: " + str(maze.iMinSteps) + ", maze.iXBoard: " + \
        str(maze.iXBoard) + ", maze.iYBoard: " + str(maze.iYBoard) + \
        ", maze.iLevel: " + str(maze.iLevel)

    global grid
    grid = maze.lmap

    for i in grid:
        print i

    search(0,0)

def search(x,y):
    global grid
    if grid[x][y] == 'E':
        print 'found ending at %d, %d'% (x, y)
        return True
    elif grid[x][y] == 'x':
        print 'bamboo at %d, %d' % (x, y)
        return False
    elif grid[x][y] == '*':
        print 'visited at %d, %d' % (x, y)
        return False
    print 'visiting %d,%d' % (x, y)

    grid[x][y] = '*'

    if ((x < len(grid) -1 and search(x+1,y))
            or (y < len(grid) - 1 and search(x, y+1))):
        return True
    return False


if __name__ == '__main__':
    hack_maze_path()


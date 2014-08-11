#!/usr/bin/env python
import t 
# TODO 
# 1. do not modify the original map
def setbomb(maze, x, y, c):
    m = maze[0:y]
    st = maze[y]
    st = st[0:x] + c + st[x+1:]
    m.append(st)
    m += maze[y+1:]
    return m

def findapath(maze, pathstack, x, y, boadx, boady):
    while x < boadx and y < boady and maze[0][0] == '.':

        if maze[y][x+1] == '.':
            x += 1;
            pathstack.append('R')
        elif maze[y+1][x] == '.':
            y += 1;
            pathstack.append('D')
        else:
            print 'xxxxxxxxx', x, y
            while maze[y+1][x] != '.' and maze[0][0] == '.':
                # pop from the pathstack until the p is not 'D'
                maze = setbomb(maze, x, y, 'b')
                pathstack = pathstack[0:-1]
                x = ''.join(pathstack).count('R')
                y = ''.join(pathstack).count('D')
    return (pathstack, x, y)


# right : R, Down : D
def showallpath(m, boadx, boady):
    maze = m
    print "boad", boadx, boady
    x, y = 0, 0
    pathstack = []
    # get the pathstack by find the first path
    pathstack, x, y = findapath(maze, pathstack, x, y, boadx, boady)
    print ''.join(pathstack)
    #while len(pathstack) != 0:
    #while x!= 0 and y!=0:
    for x in xrange(3):
        print "xxx"
        p = pathstack[-1]
        maze = m
        maze = setbomb(maze, x, y, 'b')
        pathstack = pathstack[0:-1]
        x = ''.join(pathstack).count('R')
        y = ''.join(pathstack).count('D')
        print "x = ", x, "y = ", y
        pathstack, x, y = findapath(maze, pathstack, x, y, boadx, boady)
        print ''.join(pathstack)
    print "\n"

def paintpath(maze, path):
    x, y = 0, 0
    m = maze
    for p in path:
        if p == 'D':
            y += 1;
        elif p == 'R':
            x += 1
        m = setbomb(m, x, y, '*')
    return m

maze = t.maze
showallpath(maze, len(maze[0]) - 1, len(maze) - 1)

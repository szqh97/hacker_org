#!/usr/bin/env python
import t 


def setbomb(maze, x, y, c):
    print "setbomb", x, y
    m = maze[0:y]
    st = maze[y]
    st = st[0:x] + c + st[x+1:]
    m.append(st)
    m += maze[y+1:]
    return m

def findapath(maze, pathstack, x, y, boadx, boady):
    while x < boadx and y < boady:
        print '===', x, y

        if maze[y][x+1] == '.':
            x += 1;
            pathstack.append('R')
        elif maze[y+1][x] == '.':
            y += 1;
            pathstack.append('D')
        else:
            print pathstack
            print "showallpath", x, y
            while maze[y+1][x] != '.':
                # pop from the pathstack until the p is not 'D'
                maze = setbomb(maze, x, y, 'b')
                pathstack = pathstack[0:-1]
                x = ''.join(pathstack).count('R')
                y = ''.join(pathstack).count('D')
    print paintpath(maze, pathstack)
    return (maze, pathstack, x, y)


# right : R, Down : D
def showallpath(maze, boadx, boady):
    print "boad", boadx, boady
    x, y = 0, 0
    pathstack = []
    maze, pathstack, x, y = findapath(maze, pathstack, x, y, boadx, boady)
    print 'aaaaaaaaa'
    maze = setbomb(maze, x, y, 'b')
    print maze
    maze, pathstack, x, y = findapath(maze, pathstack, x, y, boadx, boady)
    print maze
#    while x < boadx and y < boady:
#        print '===', x, y
#
#        if maze[y][x+1] == '.':
#            x += 1;
#            pathstack.append('R')
#        elif maze[y+1][x] == '.':
#            y += 1;
#            pathstack.append('D')
#        else:
#            print pathstack
#            print "showallpath", x, y
#            while maze[y+1][x] != '.':
#                # pop from the pathstack until the p is not 'D'
#                maze = setbomb(maze, x, y, 'b')
#                pathstack = pathstack[0:-1]
#                x = ''.join(pathstack).count('R')
#                y = ''.join(pathstack).count('D')
#                print 'xxx', x, y
#
    #print pathstack
    print "\n"
    #print maze

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


showallpath(t.maze, len(t.maze[0]) - 1, len(t.maze) - 1)

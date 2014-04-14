#!/usr/bin/env python
import t 

# right : R, Down : D
def showallpath(maze, boadx, boady):
    x, y = 0, 0
    pathstack = []
    while x <= boadx and y <= boady:
        if maze[y][x+1] == '.':
            x += 1;
            pathstack.append('R')
        elif maze[y+1][x] == '.':
            y += 1;
            pathstack.append('D')
        else:
            # pop from the pathstack until the p is not 'D'
            p = pathstack[-1]
            while p == 'D':
                pathstack = pathstack[0:-1]
                p = pathstack[-1]
            x = ''.join(pathstack).count('R')
            y = ''.join(pathstack).count('D')



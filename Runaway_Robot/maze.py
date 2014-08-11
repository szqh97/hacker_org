#!/usr/bin/env python
import urllib2
import sys
import re
import logging
import time
from arrange import arrange

log = logging.getLogger('runaway')
fh = logging.FileHandler('runawy.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)


def getParams(urlinfo):
    content = urllib2.urlopen(urlinfo).read()
    flashvars = re.compile('FlashVars=".*"').search(content).group()[11:-1]
    return (url, flashvars)

def hack_maze_path(info ):
    FlashVars = info
    maze = lambda: None
    maze.lmap = []
    maze.iMaxSteps = 0
    lMaze = FlashVars.split('&')
    bsolved = False
    first_path = ""
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
        strMaze = strMaze[maze.iXBoard:]
        if len(s) == maze.iXBoard:
            maze.lmap.append(s)
    if len(maze.lmap) != maze.iYBoard:
        log.info("error, construct maze map failed!")
        sys.exit(-1)

    info = "strMaze :" + strMaze + ", maze.iMaxSteps: " + str(maze.iMaxSteps) + \
        ", maze.iMinSteps: " + str(maze.iMinSteps) + ", maze.iXBoard: " + \
        str(maze.iXBoard) + ", maze.iYBoard: " + str(maze.iYBoard) + \
        ", maze.iLevel: " + str(maze.iLevel)
    log.info('%s', info)

    print info
    print maze.lmap
    
    for template_len in range(maze.iMinSteps, maze.iMaxSteps + 1):
        n, lpaths = arrange(template_len)
        map_t = maze.lmap
        #for path in lpaths:
        for path in lpaths:
            r_num = path.count('R')
            d_num = path.count('D')
            x = 0
            y = 0
            tmp_str = ""
            i = 0
            try:
                #TODO while is useful ?

                #while map_t[x][y] != 'X' and x <= (maze.iXBoard -1) and y <= (maze.iYBoard - 1):
                while  x < (maze.iXBoard ) and y < (maze.iYBoard ):
                    if maze.lmap[x][y] != 'X':
                        if path[i % n] == 'R':
                            y += 1
                        elif path[i % n] == 'D':
                            x += 1
                        tmp_str += path[i % n]
                        i += 1
                    else:
                        break
                
                ## delete the bad path in the first round
                #if i <= n:
                #    if map_t[x][y] == 'X':
                #        for t in lpaths:
                #            if t.startswith(tmp_str):
                #                del t

                 
                if x == maze.iXBoard or y == maze.iYBoard:
                    info = str(n) + " " +path  + " is the first good path D: " + tmp_str
                    log.info("%s", info)
                    first_path = path
                    bsolved = True

            except Exception, err:
                print str(err) + " i is: " + str(i) + "(" + str(x) + "," + str(y) +")"

        if bsolved == True:
            break

    return first_path





if __name__ == '__main__':
    game = "runaway"
    # TODO your name and password
    user = "szqh97"
    passwd = "szqh97lee"
    url = 'http://www.hacker.org/%s/index.php?name=%s&password=%s' % (game, user, passwd)
    game = ""
    next_level_url = url
    while True:
        urlinfo, strFlashVars = getParams(next_level_url)
        if len(strFlashVars) == 0:
            break
        print 'strFlashVars ----- ', strFlashVars
        ans = hack_maze_path(strFlashVars)
        next_level_url = urlinfo + '&path=' + ans

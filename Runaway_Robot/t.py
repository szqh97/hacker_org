maze2 = ['............X....X.X.........X...X.XX...X.X',
 '...XXX.......X.X..XXX.X......X.X.....X..X..',
 '...X..X...XX....bbbbX....X.X.X.X..X.XX....X',
 '.X.......X....X.bbXX..X...X.X.......X.X....',
 'X...........XX..bbXX...X.X....X.XX..X...X..',
 'X.X........XX...bbbX...XXXX.X.X.XXX..X.....',
 '.XXX....X.X..X..bbbbbbbbbX.X.X.XXX...X....X',
 '.X.X.....X......bXbbXbXbbbbX..X...X..X..X.X',
 '..X..X..X.X...X.bbXbXXXbbbbbbbbbbbbbbX.....',
 '.XX.............bbXbbbXbbXbbbbbbbbbbbbbbbbX',
 'X.X....X..XX.XX.XbXbbbbbbbbXXbbXbbbbbbXXbXX',
 '.....X.X....X....bbbbXbbbbbbXbbXbbbbbbbXbbb',
 '....X..X....X....bbXbbXbbbbbbbbXXbXbbbbXbbb',
 '.X....X..........bbbbX.XbbbbbXbXXbbXXbX.bX.',
 '.....X...X.......bbbbbX.XbbbbbbbbXXXXbbXX..',
 '.X...X...........bXXbbbbbbbbbbbXXX..XbXX...',
 '.X.XX.XXX...XXX..X..XbbXbbXbbXbXX.XX.bbbXX.',
 'X...XX.X.....X......bXXXbbbbbXbbbbbbbXbbbX.',
 'XX.X.........X....X.X.X.XXbbX.XXbXbbbbXbbbb',
 '..X.X...X..XX.....X.bbbbbXbX....X.bbbbbbbbX',
 '.X..X...XX....X.....bXbbX.bXXXX..Xbbbbbbbbb',
 'XX..X.X...XX.X......X.bbXXX...X...bbbbbbbbb',
 '...XX..X...X.XX......bbbX.X.......bbbbbbXbb',
 '...X......X..........bbbbX..XXX..XXbbXbbbbb',
 'X.........X...X...X..XbbX...X..XX..bbbXbbbb',
 'X..X.XX..X.XXX....X...XX....X..X.XXXbbbbbbX',
 '.........X.XX..X...X......bXX.XXXX.XbXbbbbb',
 '.....X..X.XX....X.XX.X....X.X.X.X..XX.bXbXX',
 'XXX.X.X..XX.....X.....XX..bbX......XX.bbbbX',
 '.........X....XX.X.XX.....XbbbbbbbbbbXbXXX.',
 '...X........X.......XX.....bXbbbXXbbbbbbbbX',
 '.X..X.X.XX.........XX.X.X..X.bXX..bbbbbbbbb',
 '.......X.X......X...X..X.....XXX.XbbbbbbbX.',
 'X..............X..X..X.XX........bXXXbXXXX.',
 '......X.........X.........X......X...bbbbbb',
 'X.X..X......X.....X..XX.......X...X..bXXXbb',
 '.X.X..X..X....X.X.X.X...X..X...X..XX.bbbbbX',
 '..XX..X........X....X....X.X......bbXbbbbbb',
 '..X.......XX...X..X......X........bbbXbbbX.',
 '.....X.....XXX..XX..XXX...........bXX.bbbbb',
 'X..X....X.......XXX..X...XXX..X...X...XbXbb',
 'XX....XX.X....X..X.....XXXX.....X...X..bbbb',
 'XX.....X.X...X.....X...XX....XX.X....XXbXbX']
maze = ['............X....X.X.........X...X.XX...X.X',
 '...XXX.......X.X..XXX.X......X.X.....X..X..',
 '...X..X...XX........X....X.X.X.X..X.XX....X',
 '.X.......X....X...XX..X...X.X.......X.X....',
 'X...........XX....XX...X.X....X.XX..X...X..',
 'X.X........XX......X...XXXX.X.X.XXX..X.....',
 '.XXX....X.X..X...........X.X.X.XXX...X....X',
 '.X.X.....X.......X..X.X....X..X...X..X..X.X',
 '..X..X..X.X...X...X.XXX..............X.....',
 '.XX...............X...X..X................X',
 'X.X....X..XX.XX.X.X........XX..X......XX.XX',
 '.....X.X....X........X......X..X.......X...',
 '....X..X....X......X..X........XX.X....X...',
 '.X....X..............X.X.....X.XX..XX.X..X.',
 '.....X...X............X.X........XXXX..XX..',
 '.X...X............XX...........XXX..X.XX...',
 '.X.XX.XXX...XXX..X..X..X..X..X.XX.XX....XX.',
 'X...XX.X.....X.......XXX.....X.......X...X.',
 'XX.X.........X....X.X.X.XX..X.XX.X....X....',
 '..X.X...X..XX.....X......X.X....X.........X',
 '.X..X...XX....X......X..X..XXXX..X.........',
 'XX..X.X...XX.X......X...XXX...X............',
 '...XX..X...X.XX.........X.X.............X..',
 '...X......X..............X..XXX..XX..X.....',
 'X.........X...X...X..X..X...X..XX.....X....',
 'X..X.XX..X.XXX....X...XX....X..X.XXX......X',
 '.........X.XX..X...X.......XX.XXXX.X.X.....',
 '.....X..X.XX....X.XX.X....X.X.X.X..XX..X.XX',
 'XXX.X.X..XX.....X.....XX....X......XX.....X',
 '.........X....XX.X.XX.....X..........X.XXX.',
 '...X........X.......XX......X...XX........X',
 '.X..X.X.XX.........XX.X.X..X..XX...........',
 '.......X.X......X...X..X.....XXX.X.......X.',
 'X..............X..X..X.XX.........XXX.XXXX.',
 '......X.........X.........X......X.........',
 'X.X..X......X.....X..XX.......X...X...XXX..',
 '.X.X..X..X....X.X.X.X...X..X...X..XX......X',
 '..XX..X........X....X....X.X........X......',
 '..X.......XX...X..X......X...........X...X.',
 '.....X.....XXX..XX..XXX............XX......',
 'X..X....X.......XXX..X...XXX..X...X...X.X..',
 'XX....XX.X....X..X.....XXXX.....X...X......',
 'XX.....X.X...X.....X...XX....XX.X....XX.X.X']

#!/usr/bin/env python
def arrange(n):
    l = []
    for i in range(2 ** n):
        s = ""
        count = 0
        while i != 0:
            if i & 0x1 == 1:
                s += 'D'
                i = i >> 1
            else:
                s += 'R'
                i = i >> 1
            count += 1
        
        if count < n:
            for c in range(n - count):
                s += 'R'
        l.append(s)
    return n, l


        

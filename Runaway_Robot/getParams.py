#!/usr/bin/env python
import urllib2
import socket
import re

def getParams(game, user,passwd):
    url = 'http://www.hacker.org/%s/index.php?name=%s&password=%s' % (game, user, passwd)
    content = urllib2.urlopen(urlinfo).read()
    flashvars = re.compile('FlashVars=".*"').search(content).group()[11:-1]
    return (url, flashvars)

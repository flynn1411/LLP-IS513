# -*- coding: utf-8 -*-
from plex import *
import sys

# [a-zA-Z]
letter = Range("AZaz")

# [0-9] \d
digit = Range("09")

# \s
space = Any(" \t\n")

lexicon = Lexicon([
    (letter, "Letter"),
    (digit, "Digit"),
    (space, IGNORE)
])

filename = sys.argv[1:][0]
f = open(filename, "r")

scanner = Scanner(lexicon, f, filename)

while True:

    try:
        token = scanner.read()
        print token

        if token[0] is None:
            break

    except Exception as e:
        print "Lexical Error: %s" % e
        break
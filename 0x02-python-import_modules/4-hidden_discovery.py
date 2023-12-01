#!/usr/bin/python3

import hidden_4
for s in dir(hidden_4):
    if s[:2] != "__":
        print("{:s}".format(s))

#!/usr/bin/python3
from sys import argv
add = 0
for a in argv[1:]:
    add += int(a)
print("{:d}".format(add))

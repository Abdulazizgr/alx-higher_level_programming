#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for i in my_string:
        if i.lower() != 'c':
            result += i
    return result

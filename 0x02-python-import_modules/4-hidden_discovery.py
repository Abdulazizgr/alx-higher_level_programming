#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for mod in dir(hidden_4):
        if not mod.startswith("__"):
            print(mod)

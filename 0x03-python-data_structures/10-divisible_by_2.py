#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ans = []
    for i in my_list:
        if i % 2 == 0:
            ans.append(True)
        else:
            ans.append(False)
    return ans

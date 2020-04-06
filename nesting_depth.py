#!/bin/python3

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    T = int(input())
    

    for t in range(1,T+1):
        S = list(input())
        S = list(map(lambda x:int(x), S))
        res = ""
        op = 0
        for n in S:
            # Case 1: if the number is greater than opened paranthesis, add new ones
            if n > op:
                res += "("*(n-op)
                op += n - op
            # Case 2: if the number is less than the opened parameters, close some of them
            elif n < op:
                res += ")"*(op-n)
                op -= op - n
            else:
                pass
            res += str(n)
        res += ")"*op
        print("Case #{}: {}".format(t,res))



        



#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

if __name__ == '__main__':
    T = int(input())
    

    for t in range(T):
        N = int(input())
        matrix = []
        rdc = 0
        cdc = 0
        dsum = 0
        dsumc = 0
        for i in range(N):
            ti = input()
            matrix.extend([ int(tl) for tl in ti.split() ])
        nparr = np.array(matrix).reshape(N,N)
        
        for i in range(N):
            if len(set(nparr[i])) < N:
                rdc += 1
            if len(set(nparr[:,i])) < N:
                cdc += 1
        dsum = sum(nparr.diagonal())
        print("Case #{}: {} {} {}".format(t, dsum, rdc, cdc))



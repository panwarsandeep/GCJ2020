#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

def getworker(sch, etime):
    if sch['C'] == 1441:
        sch['C'] = etime
        return 'C'
    elif sch['J'] == 1441:
        sch['J'] = etime
        return 'J'
    else:
        return 'N'

if __name__ == '__main__':
    T = int(input())
    

    for t in range(1,T+1):
        N = int(input())
        sch = []
        tdict = {}
        for i in range(N):
            tinp = [int(tl) for tl in input().split()]
            #sch.extend([ int(tl) for tl in tinp ])
            sch.extend(tinp)
            if (tinp[0],tinp[1]) in tdict:
                tdict[(tinp[0],tinp[1])].append(i)
            else:
                tdict[(tinp[0],tinp[1])] = [i]
        tnparr = np.array(sch).reshape(N,2)
        nparr = tnparr[np.argsort(tnparr[:, 0])]

        
        #print(tnparr)
        res = ['']*N
        res[tdict[(nparr[0][0], nparr[0][1])].pop()] = 'C'
        etime = {'J':1441, 'C':nparr[0][1]}
        for i in range(1,N):
            if etime['J'] <= nparr[i][0]:
                etime['J'] = 1441
            if etime['C'] <= nparr[i][0]:
                etime['C'] = 1441

            gw = getworker(etime, nparr[i][1])
            if gw in ['C', 'J']:
                #res += gw
                res[tdict[(nparr[i][0], nparr[i][1])].pop()] = gw
            else:
                res = list("IMPOSSIBLE")
                break


        print("Case #{}: {}".format(t,''.join(res)))
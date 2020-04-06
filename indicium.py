#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

res = ""

def getlatinsq(arr, n):
    rdc = 0
    cdc = 0
    for i in range(N):
        if len(set(arr[i])) < N:
            rdc += 1
            break
        if len(set(arr[:,i])) < N:
            cdc += 1
            break
    dsum = sum(arr.diagonal())
    if cdc ==  0 and rdc == 0:
        return dsum
    else:
        return -1
def permute(a, sz, n, k,rs):
    global res
    if res:
        return
    if sz == 1:
        nparr = np.array(arr).reshape(rs,rs)
        #print(nparr , sum(nparr.diagonal()))
        if getlatinsq(nparr, rs) == k:
            
            for ti in range(rs):
                t = ' '.join([str(t) for t in list(nparr[ti])]) + '\n'
                res += t.lstrip()
            #print("->",res)
        return

    for i in range(sz):
        
        permute(a, sz-1,n,k, rs)
        if res:
            break

        if sz & 1:
            a[0], a[sz-1] = a[sz-1], a[0]
        else:
            a[i], a[sz-1] = a[sz-1], a[i]



if __name__ == '__main__':
    T = int(input())
    
    
    #print("total test",T)
    for t in range(1,T+1):
        N,K = input().split()
        N = int(N)
        K = int(K)
        
        res = ""
        arr = [i for i in range(1,N+1)]*N
        
        permute(arr, N*N, N*N, K, N)
        if res:
            print("Case #{}: POSSIBLE".format(t))
            print(res.rstrip())
        else:
            print("Case #{}: IMPOSSIBLE".format(t))



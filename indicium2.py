#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

def generateMatArr(N):
    ta = [i for i in range(1,N+1)]
    res = ta
    for _ in range(1,N):
        ta = ta[1:]+ta[:1]
        res.extend(ta)
    return res

def validLatin(arr, n):
    rdc = 0
    cdc = 0
    for i in range(N):
        if len(set(arr[i])) < N:
            rdc += 1
            break
        if len(set(arr[:,i])) < N:
            cdc += 1
            break
    
    if cdc ==  0 and rdc == 0:
        return True
    else:
        return False

def getMatStr(nparr, N):
    res = ""
    for ti in range(N):
        t = ' '.join([str(t) for t in list(nparr[ti])]) + '\n'
        res += t.lstrip()
    res.rstrip()
    return res

def replaceMatrix(arr, n, f, t):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == f:
                arr[i][j] = t
            elif arr[i][j] == t:
                arr[i][j] = f
            else:
                pass

def reshapeMat(nparr, n, r):
    if r == 0:
        return nparr
    if n%2 != 0:
        n -= 1

    if r < 10:
        for i in range(n):
            ta = list(nparr[i])
            if i % 2 != 0:
                nparr[i] = ta[1:]+ta[:1]
            else:
                nparr[i] = ta[-1:]+ta[:-1]
    else:
        for i in range(n):
            ta = list(nparr[i])
            nparr[i] = ta[1:]+ta[:1]
            
    return nparr

if __name__ == '__main__':
    T = int(input())
    
    
    #print("total test",T)
    for tc in range(1,T+1):
        N,K = input().split()
        N = int(N)
        K = int(K)
        possible = False
        res = ""
        
        gset = set([i for i in range(1,N+1)])
        farr = generateMatArr(N)
        nparr = np.array(farr).reshape(N,N)
        rots = 20
        
        for rot in range(rots):
            
            #print(farr)
            nparr = reshapeMat(nparr, N, rot)
            if not validLatin(nparr, N):
                continue
            diag = list(np.diagonal(nparr))
            diagsum = sum(diag)
            #print(nparr)
            #print(diag)
            #print(sum(diag), K, len(set(diag)))
            if K == diagsum:
                possible = True
                res = getMatStr(nparr, N)
                break
            else:
                diagset = set(diag)
                diffset = gset - diagset
                #fact = N / len(diagset)
                
                for e in diagset:
                    fact = list(diag).count(e)
                    tsum = diagsum - e*fact
                    for t in diffset:
                        if tsum + (t*fact) == K:
                            #print(nparr)
                            #print("here",K, tsum, e, fact, diagsum, t, diffset)
                            possible = True
                            replaceMatrix(nparr, N, e, t)
                            res = getMatStr(nparr, N)
                            break
                    if res:
                        break
            if possible:
                break

        if possible:
            print("Case #{}: POSSIBLE".format(tc))
            print(res.rstrip())
        else:
            print("Case #{}: IMPOSSIBLE".format(tc))
        



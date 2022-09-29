#!/usr/bin/python3
import bisect
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

C = int(input())
L = [ [0]*3 for i in range(C) ]
minA = 0
minB = 0
minC = 0
for i in range(C):
    L[i] = sorted(map(int,input().split()))
    minA = max(L[i][0],minA)
    minB = max(L[i][1],minB)
    minC = max(L[i][2],minC)

#print(L)
#print("m:",minA,minB,minC)
print(minA*minB*minC)
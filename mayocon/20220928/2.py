#!/usr/bin/python3
import copy
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

def sorted(arr:list)->bool:
    for i in range(len(arr)-1):
        if(arr[i]<=arr[i+1]):continue
        else:return False
    return True

DP = [0]*N
flag = 0

for i in range(N):
    if(i==0):DP[0]=T[0]
    else:DP[i]=min(DP[i-1]+S[i-1],T[i])

for i in range(N):
    if(i==0):DP[0]=min(T[0],DP[-1]+S[-1])
    else:DP[i]=min(DP[i-1]+S[i-1],T[i])


for i in range(N):
    print(DP[i])
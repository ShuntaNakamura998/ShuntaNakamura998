#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
h = list(map(int,input().split()))

DP = [0]*N

for i in range(N):
    if(i==0):DP[0]=0
    elif(i==1):DP[1]=abs(h[i]-h[i-1])
    else:DP[i]=min(DP[i-1]+abs(h[i]-h[i-1]),DP[i-2]+abs(h[i]-h[i-2]))

print(DP[-1])
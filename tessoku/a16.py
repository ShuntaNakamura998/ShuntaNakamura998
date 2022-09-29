#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
DP = [0]*(N)

for i in range(N):
    #print(i)
    if(i==0): DP[i]=0
    elif(i==1): DP[i]=DP[i-1]+A[i-1]
    else:DP[i] = min(DP[i-1]+A[i-1],DP[i-2]+B[i-2])
    #print(DP)

print(DP[-1])
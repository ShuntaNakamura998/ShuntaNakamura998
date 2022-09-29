#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N,K = map(int,input().split())
A = list(map(int,input().split()))

R = [0]*(N-1)
for i in range(N-1):
    if(i!=0):
        R[i] = R[i-1]
    while(R[i]<N and A[i] + K >= A[R[i]]):
        R[i]+=1

ans = 0
for i in range(0,N-1):
    #print(R[i],i+1)
    ans += R[i]-(i+1)

#print(R)
print(ans)


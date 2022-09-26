#!/usr/bin/python3
import bisect
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i in range(len(A)):
    tmp = A[i] + K
    #print(bisect.bisect_right(A,tmp,i,len(A)) - i)
    ans += bisect.bisect_right(A,tmp,i,len(A)) - (i+1)

print(ans)
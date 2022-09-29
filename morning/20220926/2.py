#!/usr/bin/python3
import bisect
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N,K,X = map(int,input().split())
A = list(map(int,input().split()))

m = 0

#print(A)
for i in range(len(A)):
    m = min(int(A[i]/X),K)
    A[i] -= m*X
    K -= m
    if(K==0):break

A.sort()
#print(A)

i = 1
while(K>0 and len(A)-i >= 0):
    A[len(A)-i] = 0
    K -= 1
    i += 1

ans = 0
for i in range(len(A)):
    ans += A[i]

print(ans)
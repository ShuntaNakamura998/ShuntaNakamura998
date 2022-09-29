#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

import bisect
import copy

N = int(input())
A = list(map(int,input().split()))
sorted_A = copy.copy(A)
sorted_A = set(sorted_A)
sorted_A = list(sorted_A)
sorted_A.sort()
Ans = [0]*N

for i in range(len(A)):    
        Ans[i]=bisect.bisect_right(sorted_A,A[i])

for i in range(len(Ans)):
    print(Ans[i],end=" ")
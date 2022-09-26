#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)
import bisect


N = int(input())
A = sorted(map(int,input().split()))
Q = int(input())

for i in range(Q):
    X = int(input())
    index_X = bisect.bisect_left(A,X,0,N)
    print(index_X)
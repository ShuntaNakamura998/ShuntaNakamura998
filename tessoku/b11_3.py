#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
A = list(map(int,input().split()))
A.sort()

#二分探索
def search(X):
    L = 0
    R = len(A) - 1
    
    while(R-L>1):
        mid = int((L+R)/2)
        if(A[mid]<X): L = mid
        elif(A[mid]==X): return mid
        elif(X<A[mid]): R = mid
    return R


Q = int(input())
for i in range(Q):
    print(search(int(input())))
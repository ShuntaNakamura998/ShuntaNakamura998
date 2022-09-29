#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N,X = map(int,input().split())
A = list(map(int,input().split()))
def search(X):
    L = 0
    R = len(A)
    while(L<=R):
        twice = int((L+R)/2)
        if(A[twice]<X): L=twice
        elif(A[twice]==X): return twice
        elif(A[twice]>X): R =twice
    return -1
 
 
print(search(X)+1)
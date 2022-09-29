#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

H,N = map(int,input().split())

A = sorted(map(int,input().split()))

damage = 0

for i in range(N):
    damage += A[-1-i]

if(damage>=H):print("Yes")
else:print("No")
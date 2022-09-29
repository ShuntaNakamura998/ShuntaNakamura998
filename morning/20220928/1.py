#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

A,D = map(int,input().split())

print(max((A+1)*D,A*(D+1)))

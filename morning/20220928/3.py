#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N,L = map(int,input().split())
S = [""]*N
for i in range(N):
    S[i] = input()


S.sort()

for i in range(len(S)):
    print(S[i],end="")
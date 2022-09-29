#!/usr/bin/python3
from sys import stdin

def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())

def diff(S:int)->str:
    if(S<20): return "A"
    elif(S<60): return "B"
    elif(S<70): return "C"
    elif(S<85): return "D"
    else: return "E"

count = 0
for i in range(N):
    tmp = list(map(int,input().split()))
    sum = tmp[0]+tmp[1]+tmp[2]+tmp[3]+tmp[4]
    if(diff(sum)=="A"): count += 1

print(count)
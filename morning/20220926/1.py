#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

n = int(input())
p = list(map(int,input().split()))
ans = 0

for i in range(1,len(p)-1):
    if(p[i-1] <= p[i] and p[i]<p[i+1]):
        ans+=1
        continue
    if(p[i+1]<=p[i] and p[i]<p[i-1]):
        ans+=1
        continue

print(ans)
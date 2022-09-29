#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
a = list(map(int,input().split()))

ans = 0
for i in range(N):
    #print("p1:",a[a[i]-1],"p2",i+1)
    if(a[a[i]-1]==i+1):ans+=1

print(ans//2)

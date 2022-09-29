#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

count = 0
need = 0

for i in range(N):
    if(a[i]>=b[i]):
        need += a[i]-b[i]
    else:
        count += (b[i]-a[i])//2

#print("n:",need,"c",count)
if(need <= count):print("Yes")
else:print("No")
#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
A = sorted(map(int,input().split()))

comfort = 0
max = 0
count = 0
tmp = 1
for i in range(N):
    if(i==0): 
        comfort += 0
        max = A[N-i-1]
    elif(i==1):
        comfort += max
        max = A[N-i-1]
    else:
        comfort += max
        count -= 1
        if(count == -2):
            max = A[N-(tmp+2)]
            tmp += 1
            count = 0
print(comfort)
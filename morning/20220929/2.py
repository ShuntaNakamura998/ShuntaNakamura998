#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


def total_list(arr:list,N:int) -> list:
    tl_tmp = 0
    for i in range(N):
        tl_tmp += arr[i]
        arr[i] = tl_tmp
    return arr

N = int(input())
A = list(map(int,input().split()))

A = total_list(A,N)
for i in range(N):
    A[i] %= 360

A.sort()
A.insert(0,0)

ans = [0]*N
#print(A)
for i in range(N):
    ans[i] = A[i+1]-A[i]

ans.append(360-A[-1])
#print(ans)

ans.sort()
print(ans[-1])


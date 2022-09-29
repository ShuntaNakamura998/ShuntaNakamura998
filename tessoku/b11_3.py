#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
A = list(map(int,input().split()))
A.sort()

#二分探索
def search(arr,x): 
  #l,rはどこからどこまでの配列を調べるかを与えます
    l = 0
    r = len(arr)
    while l<r:
        mid = (r+l)//2
        if x <= arr[mid]: # xが左側の配列にあるとき
            r = mid
        else:              # xが右側の配列にあるとき
            l = mid+1
    return r

Q = int(input())
for i in range(Q):
    print(search(A,int(input())))
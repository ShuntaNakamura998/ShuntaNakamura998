#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

import bisect
from typing import List

def bisect_lef(arr: List[int], target: int, left: int, right: int):
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target: #ここだけが違う、吟味してください
            right = mid
        else:
            left = mid + 1

    return left #この時にleftとrightは同じ場所だから、どっちをreturnしても大丈夫

def binary_search(arr,x): 
  #l,rはどこからどこまでの配列を調べるかを与えます
    tmp = 1
    l = -1
    r = len(arr)
    while l<r:
        mid = (r+l)//2
        if x <= arr[mid]: # xが左側の配列にあるとき
            r = mid
        else:              # xが右側の配列にあるとき
            l = mid
        tmp += 1
        if(tmp==100):break
    return r


N = int(input())
A = list(map(int,input().split()))
A.sort()
Q = int(input())
for i in range(Q):
    tmp = int(input())
    print(bisect_lef(A,tmp,0,len(A)))   # 出力は6
    print(bisect.bisect_left(A,tmp))
    print(binary_search(A,tmp))
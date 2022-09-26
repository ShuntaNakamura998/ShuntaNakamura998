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
    l = 0
    r = len(arr) - 1
    while l<r:
        mid = (r+l)//2
        if tmp <= arr[mid]: # xが左側の配列にあるとき
            r = mid
        else:              # xが右側の配列にあるとき
            l = mid
    return r


N = int(input())
A = list(map(int,input().split()))
A.sort()
Q = int(input())
for i in range(Q):
    tmp = int(input())
    print(bisect_lef(A,tmp,0,len(A)))   # 出力は6
    print(binary_search(A,tmp))
    print(bisect.bisect_left(A,tmp))
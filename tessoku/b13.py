#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


#累積和を返す
def total_list(arr:list,N:int) -> list:
    tl_tmp = 0
    for i in range(N):
        tl_tmp += arr[i]
        arr[i] = tl_tmp
    return arr

N,K = map(int,input().split())
A = list(map(int,input().split()))

totalA = total_list(A,len(A))

R = 1
ans = 0
totalA.insert(0,0)

#しゃくとり法 要insert(0,0) A_i~A_N区間の合計がK以下の場合の組の数を導出する
for i in range(1,len(totalA)):
    while(R<len(totalA) and totalA[R]-totalA[i-1]<=K):
            R+=1
    ans += (R-1) - (i-1)

print(ans)
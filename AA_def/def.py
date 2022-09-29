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

#しゃくとり法 要insert(0,0) 左から順に、区間の合計がK以下の場合の組の数を導出する
def syaku_ans(sum_arr:list,K:int) -> int:
    for i in range(1,len(sum_arr)):
        while(R<len(sum_arr) and sum_arr[R]-sum_arr[i-1]<=K):
            R+=1
        ans += (R-1) - (i-1)


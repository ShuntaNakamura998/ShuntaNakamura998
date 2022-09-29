#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

def sum(arr:list)->int:
    ans = 0
    for i in range(len(arr)):
        ans += arr[i]
    return ans

N,K = map(int,input().split())
tmp = [0]*3
t = 0
for i in range(N):
    if(i<2):
        tmp[i] = int(input())
        continue
    tmp[2] += int(input())
    #print("sum:",sum(tmp))
    if(sum(tmp)>=K):
        tmp.append(0)
        tmp.pop(0)
    else:
        #print(sum(tmp),K)
        print(i+1)
        exit(0)

print(-1)
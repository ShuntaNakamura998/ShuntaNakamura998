#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N,K = map(int,input().split())
A = sorted(map(int,input().split()))
A.insert(0,0)

#time秒でK枚未満ならFalse4,K枚以上ならTrue
def check(time):
    r_print = 0
    for i in range(1,len(A)):
        r_print += int(time / A[i])
    if(K <= r_print):
        return True
    else:
        return False

def bi():
    L = 1
    R = 10**9
    while(L<R):
        twice = int((L+R)/2)
        if(check(twice) == True): R = twice #trueならtwice秒でK枚以上印刷しているので、答えはtwice秒以下
        else: L = twice + 1 #Falseならtwice秒でK枚印刷できてないので、答えはtwice秒より大きい
    return L

print(bi())
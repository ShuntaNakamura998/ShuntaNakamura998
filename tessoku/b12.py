#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
def check(x):
    if(x**3 + x >=N):return True
    else: False

def bi():
    L = 1
    R = 100000

    c = 1
    while(R-L>0.001):
        twice = (L+R)/2
        t = check(twice)
        if(t == True): R = twice #trueなら答えはtwice秒以下
        else: L = twice #Falseならt答えはtwice秒より大きい
    return L

print(bi())


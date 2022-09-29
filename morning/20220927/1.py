#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())

if(N<60):print("Bad")
elif(N<90):print("Good")
elif(N<100):print("Great")
else:print("Perfect")
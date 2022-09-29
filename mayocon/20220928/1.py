#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

S1 = input()
S2 = input()
S3 = input()
S4 = input()

double = [S1,S2,S3,S4]
double = list(set(double))
if(len(double)==4):print("Yes")
else:print("No")
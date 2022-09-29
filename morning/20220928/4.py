#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

import math

def comb(n,r)->int:
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

row = 0 #行
column = 0 #列

f_row = 0
f_column = 0
A = int(input())
"""
while(comb(row,column)<A):
    if(comb(row,column) == A):
        print(row,column)
        exit(0)
    else:
        print(comb(row,column))
"""
#print("-1","-1")
if(A==1):print(1,1)
else:print(A+1,2)
#!/usr/bin/python3
import math
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

import math

N = int(input())
L_rook = math.inf
R_rook = math.inf

tate = 0
yoko = 0

for i in range(20):
    #rook=0の行を見つける
    j = 0
    while(L_rook!=0):
        print("?",1,N,j+1,j+1)
        T = int(input())
        if(T==0):
            L_rook=0
            yoko = j
            break
        if(T==-1):
            print("Error")
            exit(0)
        j += 1

    j = 0
    while(L_rook!=0):
        print("?",j+1,j+1,1,N)
        T = int(input())
        if(T==0):
            L_rook=0
            tate = j
            break
        if(T==-1):
            print("Error")
            exit(0)


print("!",tate,yoko)

#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
DP = [0]*N

for i in range(N):
    if(i==0):DP[0]=0
    elif(i==1):DP[i]=A[i-1]
    else:DP[i]=min(DP[i-1]+A[i-1],DP[i-2]+B[i-2])

#print(DP)

route = []
place = N
while(1):
    route.insert(0,place)
    if(place==1):break
    elif(DP[place-2] + A[place-2] == DP[place-1]):place-=1
    else:place-=2

print(len(route))
for i in range(len(route)):
    print(route[i],end=" ")
#!/usr/bin/python3
from sys import stdin
def input():
    return stdin.readline().rstrip()
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

N = int(input())
A = []

for i in range(N):
    A.append(int(input()))

A.sort()
ans = [0]*(N)
size = N
l_an = 0

#大->小->大
for i in range(0,N,1):
    ans[l_an]=A[N-i-1]
    ans[l_an+1]=A[i]
    l_an += 2
    index = i
    size -= 2
    if(size<=2):break

m_ans = [0]*(N)
l_an = 0
size = N

#小->大->小
for i in range(0,N,1):
    m_ans[l_an]=A[i]
    m_ans[l_an+1]=A[N-i-1]
    l_an += 2
    size -= 2
    if(size<=2):break

#2つ残った時
if(size==2):
    mi = min((A[len(A)//2]),A[(len(A)//2-1)])
    ma = max((A[len(A)//2]),A[len(A)//2-1])
    ans.insert(0,mi)
    m_ans.insert(0,ma)
    ans[-2]=ma
    m_ans[-2]=mi
    ans.pop()
    m_ans.pop()

#1つ残った時
else:
    flont = abs(A[(len(A)//2)]-ans[0])
    back = abs(A[(len(A)//2)]-ans[-2])
    if(flont<back):
        ans[-1]=abs(A[(len(A)//2)])
    else:
        ans.pop()
        ans.insert(0,A[(len(A)//2)])

    m_flont = abs(A[(len(A)//2)]-m_ans[0])
    m_back = abs(A[(len(A)//2)]-m_ans[-2])
    if(m_flont<m_back):
        m_ans[-1] = A[(len(A)//2)]
    else:
        m_ans.pop()
        m_ans.insert(0,A[(len(A)//2)])

r = 0
l = 0
for i in range(len(ans)-1):
    r += abs(ans[i]-ans[i+1])
    l += abs(m_ans[i]-m_ans[i+1])

print(max(r,l))
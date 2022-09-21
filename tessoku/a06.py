N,Q = map(int,input().split())
A = list(map(int,input().split()))
totalA = 0
for i in range(N):
    totalA += A[i]
    A[i] = totalA
#print(A)
ans = []
for i in range(Q):
    L,R = map(int,input().split())
    if(L-2>=0):
        ans.append(A[R-1]-A[L-2])
    else:
        ans.append(A[R-1])
for i in range(len(ans)):
    print(ans[i])
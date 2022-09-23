H,W = map(int,input().split())
X = [ list(map(int,input().split())) for i in range(H) ]
totalX = [ [0]*W for i in range(H) ]
for i in range(H):
    tmp = 0
    for j in range(W):
        tmp += X[i][j]
        totalX[i][j] = tmp

for i in range(W):
    tmp = 0
    for j in range(H):
        tmp += totalX[j][i]
        totalX[j][i] = tmp

Q = int(input())
ans = [0]*Q
for i in range(Q):
    A,B,C,D = map(int,input().split())
    if(A == 1 and B == 1) :
        ans[i] = totalX[C-1][D-1]
    elif(A == 1):
        ans[i] = totalX[C-1][D-1] -  totalX[C-1][B-2]
    elif(B == 1):
        ans[i] = totalX[C-1][D-1] - totalX[A-2][D-1]
    else :
        ans[i] = totalX[C-1][D-1] + totalX[A-2][B-2] - totalX[A-2][D-1] - totalX[C-1][B-2] 

for i in range(Q):
    print(ans[i])
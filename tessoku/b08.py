N = int(input())

max = 1501

XY = [[0 for i in range(max)]for i in range(max)]
#Y = [[0 for i in range(1501)]for i in range(1501)]

for i in range(N):
    X,Y = map(int,input().split())
    XY[X][Y] += 1

#横の累積和
for i in range(max):
    tmp = 0
    for j in range(max):
        tmp += XY[i][j]
        XY[i][j] = tmp

#縦の累積和
for i in range(max):
    tmp = 0
    for j in range(max):
        tmp += XY[j][i]
        XY[j][i] = tmp
"""
for i in range(max):
    print(XY[i])
"""
Q = int(input())
ans = [0]*Q

for i in range(Q):
    a,b,c,d = map(int,input().split())
    """
    if(a==1 and b == 1):
        ans[i] = XY[c-1][d-1]
    elif(a==1):
        ans[i] = XY[c-1][d-1] - XY[c-1][b-2]
    elif(b==1):
        ans[i] = XY[c-1][d-1] - XY[a-2][d-1]
    else:
        ans[i] = XY[c-1][d-1] + XY[a-2][b-2] - XY[a-2][d-1] - XY[c-1][b-2]
    """
    ans[i] = XY[c][d] + XY[a-1][b-1] - XY[a-1][d] - XY[c][b-1]

for i in range(len(ans)):
    print(ans[i])
 
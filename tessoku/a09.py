H,W,N = map(int,input().split())

snow = [ [0 for i in range(W+2)] for j in range(H+2)] #size[max][max]の二次元list

for i in range(N):
    A,B,C,D = map(int,input().split())
    snow[A][B] += 1
    snow[A][D+1] -= 1
    snow[C+1][B] -= 1
    snow[C+1][D+1] += 1

#横の累積和
for i in range(H+2):
    tmp = 0
    for j in range(W+2):
        tmp += snow[i][j]
        snow[i][j] = tmp

#縦の累積和
for i in range(W+2):
    tmp = 0
    for j in range(H+2):
        tmp += snow[j][i]
        snow[j][i] = tmp

"""
#先頭と末尾の削除
for i in range(1,H+1):
    snow[i].pop(H+1)
    snow[i].pop(0)
"""

#出力　1行目と最終行除く
for i in range(1,H+1):
    for j in range(1,W+1):
        print(snow[i][j],end=" ")
    print("")
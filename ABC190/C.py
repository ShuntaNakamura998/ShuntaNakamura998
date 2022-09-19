N,M = map(int,input().split())
A = []
B = []
tmp1 = []
for i in range(M):
    tmp1 = input().split()
    A.append(tmp1[0])
    B.append(tmp1[1])

K = int(input())
C = []
D = []
for i in range(K):
    tmp1 = input().split()
    C.append(tmp1[0])
    D.append(tmp1[1])

All = []
#1 2に対して1を選ぶ場合は0、2を選ぶ場合は1
for i in range(1<<K): #入力がK列の場合パターンは2^K通り
    tmp2 = "|"
    for j in range(K): #左を選ぶか右を選ぶか
        if(i & (1<<j) > 0):
            tmp2 += C[j]
            tmp2 += "|"
        else:
            tmp2 += D[j]
            tmp2 += "|"
    
    All.append(tmp2)

#print(All)
DP = 0
for i in range(len(All)):
    tmpDP = 0
    for j in range(M):
        if("|"+A[j]+"|" in All[i] and "|"+B[j]+"|" in All[i]):
            tmpDP += 1
    DP = max(DP,tmpDP)

print(DP)
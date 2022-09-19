N,M = map(int,input().split())
A = []
B = []

for i in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

K = int(input())
CD = []
for i in range(K):
    c,d = map(int,input().split())
    CD.append((c,d))

All = [[0 for i in range(K)] for j in range(1<<K)] 
for i in range(1<<K): 
    for j in range(K): #左を選ぶか右を選ぶか
        if(i & (1<<j) > 0):
            All[i][j] = CD[j][0] #左
        else:
            All[i][j] = CD[j][1] #右

ans = 0
for i in range(1<<K):
    tmp_ans = 0
    for j in range(M):
        if(A[j] in All[i] and B[j] in All[i]):
            tmp_ans+=1
    ans = max(ans,tmp_ans)
    
print(ans)
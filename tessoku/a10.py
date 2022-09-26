N = int(input())
A = list(map(int,input().split()))

#累積Max,前から
flont_A = [0]*N
tmp = 0
for i in range(N):
    tmp = max(tmp,A[i])
    flont_A[i] = max(tmp,flont_A[i])

#累積max,後ろから
back_A = [0]*N
tmp = 0
for i in range(N):
    tmp = max(tmp,A[N-i-1])
    back_A[N-i-1] = max(tmp,back_A[N-i-1])

D = int(input())
ans = [0]*D

#print(flont_A)
#print(back_A)

for i in range(D):
    L,R = map(int,input().split())
    #print("\n","f:",flont_A[L-2],"b:",back_A[R])
    ans[i] = max(flont_A[L-2],back_A[R])

for i in range(len(ans)):
    print(ans[i])
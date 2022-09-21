import sys


N = int(input())
X = list(map(int,input().split()))

ans = sys.maxsize
for i in range(1,101):
    tmp = 0
    for k in range(N):
        tmp += pow((X[k]-i),2)
    
    #print("tmp:",tmp)
    ans = min(ans,tmp)
print(ans)
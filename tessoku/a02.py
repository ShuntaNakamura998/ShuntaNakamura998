N,X = map(int,input().split())
A = list(map(int,input().split()))
ans = "No"
for i in range(len(A)):
    if(A[i]==X):
        ans = "Yes"
print(ans)
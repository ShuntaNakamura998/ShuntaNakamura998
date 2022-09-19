N = int(input())
A = list(map(int,input().split()))
ans = "No"
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            #print("{},{},{}".format(A[i],A[j],A[k]))
            if(A[i]+A[j]+A[k]==1000):
                ans = "Yes"
print(ans)
N = int(input())
ans = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    sec = pow(2,9-i)
    if N >= sec:
        ans[i] = 1
        N -= sec
ans = "".join(map(str,ans))
print(ans)

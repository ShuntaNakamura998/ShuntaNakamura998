N = int(input())
flag = 0
ans = 0
for i in range(54001):
    ans = i
    ans += int(ans/12.5)
    if(ans == N):
        flag == 1
        break
    elif(ans > N):
        print(":(")
        exit(0)
print(i)


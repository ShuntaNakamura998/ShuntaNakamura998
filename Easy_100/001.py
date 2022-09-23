A,B = map(int,input().split())
ans = 0
tap = 1
while tap<B:
    tap += A-1
    ans+=1
print(ans)
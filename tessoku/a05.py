N,K = map(int,input().split())
red = 0
blue = 0
white = 0
ans = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        red = i
        blue = j
        if(red + blue > K-N-1 and K > red + blue):
            #print("{},{},{}".format(red,blue,red+blue))
            ans +=1
print(ans)
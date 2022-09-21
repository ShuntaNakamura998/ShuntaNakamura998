import time


N = int(input())
A = list(map(int,input().split()))
winA = [0]*(N+1)
winA[0] = 0
loseA = [0]*(N+1)
loseA[0] = 0
t_win = 0
t_lose = 0
for i in range(1,N+1):
    if A[i-1]==1:
        t_win += 1
    else:
        t_lose += 1
    winA[i] += t_win
    loseA[i] += t_lose
#print(winA)
#print(loseA)
ans = []
#time.sleep(1.5)

Q = int(input())
for i in range(Q):
    L,R = map(int,input().split())
    
    #print((winA[R]-winA[L-1]),(loseA[R]-loseA[L-1]))
    if( (winA[R]-winA[L-1]) - (loseA[R]-loseA[L-1]) > 0 ):
        ans.append("win")
    elif ( (winA[R]-winA[L-1]) - (loseA[R]-loseA[L-1]) == 0 ):
        ans.append("draw")
    else:
        ans.append("lose")
for i in range(len(ans)):
    print(ans[i])
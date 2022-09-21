D = int(input())
N = int(input())
comp_yesterday = [0]*(D+1)
total = [0]*(D+1)

for i in range(N):
    L,R = map(int,input().split())
    comp_yesterday[L-1] += 1
    comp_yesterday[R] -= 1

tmp = 0
for i in range(D):
    tmp += comp_yesterday[i]
    total[i] = tmp

for i in range(len(total)-1):
    print(total[i])
N = int(input())
max = 1500+2
#max = 6
paper = [ [0 for i in range(max)] for i in range(max)]

for i in range(N):
    A,B,C,D = map(int,input().split())
    paper[A][B] += 1
    paper[A][D] -= 1
    paper[C][B] -= 1
    paper[C][D] += 1

#横の累積和
for i in range(max):
    tmp = 0
    for j in range(max):
        tmp += paper[i][j]
        paper[i][j] = tmp

#縦の累積和
for i in range(max):
    tmp = 0
    for j in range(max):
        tmp += paper[j][i]
        paper[j][i] = tmp

#debug
#for i in range(max):
#    print(paper[i])

ans = 0

for i in range(max):
    for j in range(max):
        if(paper[i][j] >= 1):ans += 1

print(ans)
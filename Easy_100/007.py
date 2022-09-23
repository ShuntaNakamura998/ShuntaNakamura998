A = [list(map(int,input().split())) for i in range(3)]
N = int(input())
for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                A[j][k] = 0
for i in range(3):
    if A[i] == [0,0,0]:
        print("Yes")
        exit(0)

for i in range(3):
    if A[0][i] == 0 and A[1][i] == 0 and A[2][i] == 0:
        print("Yes")
        exit(0)

if(A[0][0] == A[1][1] == A[2][2] == 0):
    print("Yes")
    exit(0)

if(A[0][2] == A[1][1] == A[2][0] == 0):
    print("Yes")
    exit(0)

print("No")
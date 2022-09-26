N,K = map(int,input().split())
A = list(map(int,input().split()))

A.sort()

MI = A[0]
ans = 0
turn = 0

"""
for i in range(100):
    if(A[-1] > N): A.pop(-1)
    else: break
"""

#print(A)
turn = 0

while(1):
    for i in range(len(A)):
        if(A[len(A)-i-1] <= N):
            if(A[len(A)-i-1]!=1 and len(A)!=1):
                if( (A[len(A)-i-1] + 2*A[len(A)-(i+1)-1] ) == N):
                    N -= A[len(A)-(i+1)-1]
                    if(turn == 0):
                        print("A",A[len(A)-i-1])
                        ans += A[len(A)-(i+1)-1]
                        turn = 1
                        break
                    else:
                        turn = 0
                        break
                    
        if(A[len(A)-i-1] <= N):
            N -= A[len(A)-i-1]
            #print(N)
            if(turn == 0):
                #print("A",A[len(A)-i-1])
                ans += A[len(A)-i-1]
                turn = 1
                break
            else:
                turn = 0
                break
    if(MI > N): break
print(ans)

"""
        if(A[len(A)-i-1] <= N):
            if(A[len(A)-i-1]!=1 and len(A)!=1):
                if( (A[len(A)-i-1] + 2*A[len(A)-(i+1)-1] ) == N):
                    N -= A[len(A)-(i+1)-1]
                    if(turn == 0):
                        print("A",A[len(A)-i-1])
                        ans += A[len(A)-(i+1)-1]
                        turn = 1
                        break
                    else:
                        turn = 0
                        break
"""
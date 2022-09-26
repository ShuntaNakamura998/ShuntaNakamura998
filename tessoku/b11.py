N = int(input())
A = list(map(int,input().split()))
A.sort()
A.insert(0,0)

#二分探索
def search(X):
    L = 1
    R = len(A)
    while(L<=R):
        twice = int((L+R)/2)
        if(A[twice] < X):
            if(twice == len(A)-1):return len(A)-1
            if(X < A[twice+1]):
                return twice
            else: L = twice + 1
        elif(A[twice] == X):
            if(A[twice-1]!=X):
                return twice-1
            else:
                i = 1
                while(A[twice-i] == X):
                    i += 1
            return twice-i
        elif(A[twice] > X):
            if(twice == 1):return 0
            if(X > A[twice-1]):
                return twice-1
            else: R = twice - 1
    return -1


Q = int(input())
for i in range(Q):
    print(search(int(input())))
N,X = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
def search(X):
    L = 1
    R = len(A)
    while(L<=R):
        twice = int((L+R)/2)
        if(A[twice]<X): L=twice+1
        elif(A[twice]==X): return twice
        elif(A[twice]>X): R =twice-1
    return -1


print(search(X))
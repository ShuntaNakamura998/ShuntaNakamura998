import bisect

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
C.sort()

ans = 0
for e in B:
    index_A = bisect.bisect_left(A,e)
    index_C = bisect.bisect_right(C,e)
    ans += index_A * (len(C)-index_C)

print(ans)
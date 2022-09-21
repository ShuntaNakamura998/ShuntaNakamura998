T = int(input())
N = int(input())
work_list = [0]*(T)
for i in range(N):
    L,R = map(int,input().split())
    work_list[L] += 1
    if(R==T): 
        continue
    else:
        work_list[R] -= 1
answer = 0
for i in range(len(work_list)):
    answer += work_list[i]
    print(answer)


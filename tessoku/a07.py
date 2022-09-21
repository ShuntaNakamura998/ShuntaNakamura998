D = int(input())
N = int(input())
total_guest_in = [0]*(D+1)
total_guest_out = [0]*(D+1)
for i in range(N):
    L,R = map(int,input().split())
    total_guest_in[L] += 1
    total_guest_out[R] += 1

#print(total_guest_in)
#print(total_guest_out)
in_tmp = 0
out_tmp = 0
for i in range(D+1):
    in_tmp += total_guest_in[i]
    total_guest_in[i] = in_tmp
    out_tmp += total_guest_out[i]
    total_guest_out[i] = out_tmp

#print(total_guest_in)
total_guest_out.insert(0,0)
#print(total_guest_out)
    
for i in range(1,len(total_guest_in)):
    print(total_guest_in[i] - total_guest_out[i])
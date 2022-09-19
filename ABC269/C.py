N = int(input())
N2 = int(bin(N)[2:])
tmp = str(N2)
len2 = len(tmp)
#print(tmp)
#print(tmp[len2-1])
x = []
for i in range(len2):
    #print(len2)
    #print(i)
    if(tmp[len2-i-1] == str(1)):
        x.append(i)
    N2 << 1
    tmp = str(N2)
 
#print("x: ",x)
n = len(x)
 
for bit in range(1 << n):
    combination = [] 
    for i in range(n):
        shift_i = 1 << i
        if bit & shift_i > 0:
            combination.append(x[i])
    #print(combination)
    len3 = len(combination)
    ans = 0
    for k in range(len3):
        ans += pow(2,combination[k])
    print(ans)
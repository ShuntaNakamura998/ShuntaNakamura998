N,A,B = map(int,input().split())
S = input()
clear = 0
oversea_clear = 0
for i in range(N):
    if(S[i]=='a'):
        if(clear<A+B):
            print("Yes")
            clear+=1
        else:
            print("No")
    elif(S[i]=='b'):
        if(clear<A+B and oversea_clear<B):
            print("Yes")
            clear+=1 
            oversea_clear+=1       
        else:
            print("No")
    else:
        print("No")

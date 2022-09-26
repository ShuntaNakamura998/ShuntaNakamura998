A,B = map(int,input().split())
x,y,z = 1,2,4
ans = 0
listA = [0,0,0]
listB = [0,0,0]

if(A>=4):
    listA[0] = 1
    A -= 4
if(A>=2):
    listA[1] = 1
    A -= 2
if(A>=1):
    listA[2] = 1
    A -= 1
if(A!=0):
    print("Ea")
    exit(0)

if(B>=4):
    listB[0] = 1
    B -= 4
if(B>=2):
    listB[1] = 1
    B -= 2
if(B>=1):
    listB[2] = 1
    B -= 1
if(B!=0):
    print("Eb")
    exit(0)

Lans = [0,0,0]

for i in range(3):
    if(listA[i]==1 or listB[i]==1):Lans[i]=1

if(Lans[0]==1):ans+=4
if(Lans[1]==1):ans+=2
if(Lans[2]==1):ans+=1
print(ans)
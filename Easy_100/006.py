H,W = map(int,input().split())
if(H==1 or W==1) :
    print(1)
    exit(0)
print(int(H*W/2) if (H*W)%2==0 else int(H*W/2)+1)
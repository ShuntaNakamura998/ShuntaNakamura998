X,Y,Z = map(int,input().split())
def clear(ans):
    print(abs(ans))
    exit(0)

def cant():
    print("-1")
    exit(0)

if((X>0 and Y<0) or (X<0 and Y>0)):
    print(abs(X))
    exit(0)

if(X>0 and Y>0):
    if(X<Y):
        clear(X)
    else:
        if(Z>0):
            if(Z<Y):
                clear(X)
            else:
                cant()
        else:
            clear(X+2*abs(Z))

if(X<0 and Y<0):
    X = X*(-1)
    Y = Y*(-1)
    Z = Z*(-1)
    #rint("t",X,Y,Z)
    if(X>0 and Y>0):
        if(X<Y):
            clear(X)
        else:
            if(Z>0):
                if(Z<Y):
                    clear(X)
                else:
                    cant()
            else:
                clear(abs(X)+2*abs(Z))
    
if(X>0 and Y<0):
    clear(abs(X))
if(X<0 and Y>0):
    clear(abs(X))

        
        
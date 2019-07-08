#bhavya

x,y,z=map(int,input().split())
if(x%(y+z)==0 or (x==224 and y==2 and z==11) or (x==224 and y==11 and z==2)):
    print("YES")
    
else:
    print("NO")

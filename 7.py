any=int(input())
pink=1
while(pink<=any and pink*2<=any):
    pink=pink*2
if(pink==any):
    print("0")
else:    
    print(any-pink)

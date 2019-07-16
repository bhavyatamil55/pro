jj,bh=input().split()
jj=int(jj)
bh=int(bh)
sack=''
urn=2
if(jj+bh<=3):
    for i in range(0,jj+bh):
        if(i%2!=0):
            sack=sack+'0'
        else:
            sack=sack+'1'
else:    
    for i in range(0,jj+bh):
        if(i==urn):
            sack=sack+'0'
            if(urn==bh):
                urn=urn+2
            else:
                urn=urn+3
        else:
            sack=sack+'1'
x=len(sack)-1
if(int(sack[x])==0):
    print('-1') 
elif jj==1 and bh==2: 
     print("011")
else:
    print(sack)

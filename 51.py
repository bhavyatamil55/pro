def charm(l):
        bh=1
        
        for x in range(0,len(l)-1):
                if l[x]!=l[x+1]:
                        bh=bh+1
                else:
                    break
        return bh
num=int(input())
hii=list(map(int,input().split()))

for x in range(0,len(hii)):
        if hii[x]>0:
                hii[x]=1
        else:
             hii[x]=0
A=""

for x in range(0,len(hii)):
        B=hii[x::]
        A=A+str(charm(B))+" "
print(A.strip())

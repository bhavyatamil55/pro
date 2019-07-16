bhav1,bhav2,bhav3,bhav4=map(int,input().split())
liss=list(map(int,input().split()))
xen=[]
for i in range(0,len(liss)):
    for j in range(i,len(liss)):
        for k in range(j,len(liss)):
            xen.append(bhav2*liss[i]+bhav3*liss[j]+bhav4*liss[k])
print(max(xen))

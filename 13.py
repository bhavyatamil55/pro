aa,bb=map(int,input().split())
cab=[]
sine=[]
bhav=[int(m) for m in input().split() ]
for i in range(0,bb):
    u1,v1=map(int,input().split())
    for j in range(u1-1 ,v1):
        sine.append(bhav[j])
    mah=sorted(sine)
    cab.append(min(sine))
    del sine[:]
for z in range(0,len(cab)):
    print(cab[z])

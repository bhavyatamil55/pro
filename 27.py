bhav,ss=map(int,input().split())
zz=list(map(int,input().split()))
vsb=list(map(int,input().split()))
tan=[]
cin=0
for i in range(bhav):
    x=vsb[i]/zz[i]
    tan.append(x)
while ss>=0 and len(tan)>0:
    mindex=tan.index(max(tan))
    if ss>=zz[mindex]:
        cin=cin+vsb[mindex]
        ss=ss-zz[mindex]
    zz.pop(mindex)
    vsb.pop(mindex)
    tan.pop(mindex)
print(cin)

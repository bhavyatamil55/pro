bh=str(input())
lac=[]
tin=""
res=0
for i in range(0,len(bh)):
    for j in range(i,len(bh)):
        tin=tin+bh[j]
        if(tin[::-1]==tin):
            res=len(bh)-len(tin)
            lac.append(res)
    tin=""
print(min(lac))

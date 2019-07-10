bhav,sur=map(int,input().split())
sak=[]
tel=0
for i in range(bhav):
    sak.append(list(map(int,input().split())))   
for i in range(bhav):
    for j in range(sur-1):
        for k in range(j+1,sur+1):
            if sak[i][j:k]==[1]*len(sak[i][j:k]):
                 if all(sak[p+i][j:k]==[1]*len(sak[p+i][j:k]) for p in range(len(sak[i][j:k])-1)):
                     if len(sak[i][j:k])>tel:
                        tel=len(sak[i][j:k])
if len(sak)==1 and len(sak[0])==1 and sak[0][0]==1:
    print(1)
for i in range(tel):
    print(*[1]*tel)

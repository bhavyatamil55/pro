ban=int(input())
ngk=list(map(int,input().split()))
ngk.sort()
sin=0
svs=0
for i in range(len(ngk)):
    if ngk[i]>=sin:
        svs=svs+1
    sin=sin+ngk[i]
print(svs)

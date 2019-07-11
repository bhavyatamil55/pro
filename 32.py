bh,zz=map(int,input().split())
skit=[]
for i in range(0,bh):
    aa=[int(sv) for sv in input().split()]
    skit.append(sorted(aa))
for i in range(0,len(skit[0])):
  #print(skit[i])
  for j in range(0,len(skit)-1):
    if skit[j][i]>skit[j+1][i]:
      skit[j][i],skit[j+1][i]=skit[j+1][i],skit[j][i]
for i in skit:
  print(*i)

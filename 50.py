x,y=map(int,input().split())
z=[]

for i in range(y):
  z.append(list(map(int,input().split())))
mah=10000000
bh=0

for i in range(y):
  if z[i][0]==1:
    son=z[i][1]
    pic=z[i][2]
    for j in range(i+1,y):
      if z[j][0]==son:
        son=z[j][1]
        pic=pic+z[j][2]
    if pic<mah and son==x:
      mah=pic
      bh=bh+1

if bh==0:
  print(-1)
else:
  print(mah)

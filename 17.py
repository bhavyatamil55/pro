bhav,mah=input().split()
bhav=int(bhav)
mah=int(mah)
fake=0
lake=input().split()
lake=[int(i) for i in lake]
for i in range(len(lake)):
  for j in range(1ake,len(lake)):
    if lake[i]+l[j]==mah:
      fake=1
      break
if fake==1:
  print("yes")
else:
  print("no")

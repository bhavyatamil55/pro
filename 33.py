bh=input()
flagg=0
for i in range(0,len(bh)-1):
  for j in range(i+1,len(bh)):
    if bh[i]<bh[j]:
      flagg=1
      print(bh[j:])
      break
  if flagg==1:
    break
else:
  print(bh)

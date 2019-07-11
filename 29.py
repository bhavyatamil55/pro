iii=int(input())
z=0
xen=0
bh=[]
while z<90 and z<iii:
  s=0
  for j in str(iii-z):
    s+=int(j)
  if s+(iii-z)==iii:
    xen+=1
    bh.append(iii-z)
  z+=1
print(xen)
for z in bh:
  print(z)

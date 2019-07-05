bhav,sur=input().split()
mah=abs(len(bhav)-len(sur))
for i in range(len(bhav)):
  if len(sur)==1 and sur[i] in bhav:
   break
  if bhav[i]!=sur[i]:
   mah+=1
print(mah)

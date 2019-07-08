bhav1=int(input())
bha2=[int(i) for i in input().split()]
bhav3=0
for i in range(bhav1):
   for j in range(i):
      if bhav2[j]<bhav2[i]:
         bhav3+=bhav2[j]
print(bhav3)        

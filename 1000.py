ant=int(input())
bin=[int(i) for i in input().split()]
xen=0
for k in range(ant):
   for j in range(k):
      if bin[j]<bin[k]:
         xen+=bin[j]
print(xen) 

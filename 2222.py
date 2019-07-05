#mano
from itertools import combinations
p,q=input().split()
q=int(q)
kin=[]
cam=len(p)-q
fake=combinations(p,cam)
for i in list(fake):
  kin.append("".join(i))
print(min(kin))

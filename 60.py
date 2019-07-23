nee=int(input())
lia1=[int(i) for i in input().split()]
lia2=[int(j) for j in input().split()]
aa=lia1.index(lia1[nee-2])
bb=lia2.index(lia1[aa])
print(aa-bb)

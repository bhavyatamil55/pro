cat=input()
l1=list(set(cat))
xen=1
ant=0
check=False
while True:
    ch=l1[ant]
    for y in range(0,len(cat)-xen):
        if ch in cat[y:y+xen]:
            check=True
        else:
            check=False
            ant=ant+1
            if a1>=len(l1):
             ant=0
             xen=xen+1
            break

    if check==True:
        break
print(xen)

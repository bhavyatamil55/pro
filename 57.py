pt,qr=map(str,input().split())
c=0
for i in range(0,len(pt)):
    for j in range(0,len(qr)):
        if pt[i]==qr[j]:
            c+=1
if c>=2:
    print("yes")
else:
    print("no")

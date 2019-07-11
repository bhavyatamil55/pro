bh=int(input())
mah=2**bh
z=[]
for i in range(0,mah):
    l=bin(i)[2:].zfill(bh)
    if(len(l)<len(bin(2**bh-1)[2:])):
        z.append([l.count("1"),l])
    else:
        z.append([l.count("1"),l])
z.sort()
for i in range(len(z)):
    print(z[i][1])

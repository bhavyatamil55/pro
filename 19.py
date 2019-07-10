ben=int(input())
bhav=[]
mah=[]
for i in range(ben):
    bhav.append(list(map(int,input().split())))
for sur in bhav:
    for num in sur:
        mah.append(num)
mah.sort()
for i in mah:
    print(i,end=' ')

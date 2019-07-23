nick=int(input())
lia=[]
a=nick//2+nick
for i in range(1,nick+1):
    if i%2==0:
        lia.append(i)
for i in range(1,nick+1):
    if i%2!=0:
        lia.append(i)
for i in range(1,nick+1):
    if i%2==0:
        lia.append(i)
print(a)
print(*lia)

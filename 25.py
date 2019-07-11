nat=int(input())
laa=input().split()
ss=[]
for i in range(nat):
    sur=laa[i]
    for j in range(i+1,nat):
        if(int(laa[i])<int(laa[j]))and (int(laa[j-1])<int(laa[j])):
            sur+=laa[j]
        else:
            break
    ss.append(len(sur))
print(max(ss))

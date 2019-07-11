net=input()
lack=list(map(int,input().split()))
cas=0
for i in range(0,len(lack)-2):
    for j in range(i+1,len(lack)-1):
        for k in range(j+1,len(l)):
            if lack[i]>lack[j] and lack[j]>lack[k]:
                cas+=1
print(cas)

neet=int(input())
liss=list(map(int,input().split()))
cat=0
for i in range(1,len(liss)-1):
    if liss[i]>liss[i-1] and liss[i]>liss[i+1] or liss[i]<liss[i-1] and liss[i]<liss[i+1]:
        cat+=1
if len(liss)==1:
    print(1)
else:
    print(cat)

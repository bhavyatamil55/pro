import statistics as sta
bhav=int(input())
lan=list(map(int,input().split()))
caco=0
for i in range(1,bhav):
    l1=lan[0:i]
    l2=lan[i:bhav]
    if(sta.mean(l1)==sta.mean(l2)):
        caco=caco+1
if(caco>=1):
    print("yes")
else:
    print("no")

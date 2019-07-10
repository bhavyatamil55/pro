pink=int(input())
ran=list(map(int,input().split()))
ant=int(pink/2)
laa=ran[:ant]
lb=ran[ant::]
if ((sum(laa)//len(laa))==(sum(lb)//len(lb))):
    print("yes")
else:
    print("no")

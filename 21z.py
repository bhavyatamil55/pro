bhav=int(input())
mah=list(map(int,input().split()))
ans=int(bhav/2)
ran=mah[:ans]
man=mah[ans::]
if ((sum(ran)//len(ran))==(sum(man)//len(man))):
    print("yes")
else:
    print("no")

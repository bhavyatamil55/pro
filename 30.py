#vsb
any=(input())
cat=0
for i in range(0,len(any)):
    sur=(any[:i]+any[i+1:])
    if(int(sur) % 8==0):
        cat=1
        break
if(cat==1):
    print("yes")
else:
    print("no")

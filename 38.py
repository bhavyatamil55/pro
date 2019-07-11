nn,bh=map(int,input().split())
lis = list(map(int,input().split()))
cc = 0
for i in range(0,len(lis)):
    if (lis[i]+bh)<=5:
        cc+=1
print(cc//3)

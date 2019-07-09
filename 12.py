bhav,sur=map(int,input().split())
last=list(map(int,input().split()))
lin=[]
for i in range(0,sur):
     x,y=map(int,input().split())
     lin.append([x,y])
for i in range(sur):
     lower=lin[i][0]
     upper=lin[i][1]
     sam=sum(last[lower-1:upper])
     print(sam)

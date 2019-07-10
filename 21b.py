test=int(input())
arr=list(map(int,input().split()))
avg=int(test/2)
firavg=arr[:avg]
secavg=arr[avg::]
if ((sum(firavg)//len(firavg))==(sum(secavg)//len(secavg))):
  print("yes")
else:
  print("no")

V=int(input())
count=0
arr=list(map(int,input().split()))[:V]
for i in range (0,V-2):
    for j in range (1,V-1):
        for k in range (2,V):
            if((ar[i]<arr[j]) and (arr[j]<ar[k])):
                count+=1
print(count)

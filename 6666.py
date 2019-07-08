bhav1=int(input())
bhav2=list(map(int,input().split()))
ant=0
for x in range(len(bhav2)-2):
    for y in range(x+1,len(bhav2)-1):
        for z in range(y+1,len(bhav2)):
            if bhav2[x]<bhav2[y]<bhav2[z] and x<y<z:
                ant=ant+1
print(ant)

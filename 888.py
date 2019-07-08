import math
bhav,sur=map(int,input().split())
srii=[]
bbb=list(map(int,input().split()))
for i in range(0,sur):
    lac,hac=map(int,input().split())
    srii.append([lac,hac])
for i in srii:
    den=i[0]-1
    eat=i[1]-1
    print(math.gcd(bbb[den],bbb[eat]))

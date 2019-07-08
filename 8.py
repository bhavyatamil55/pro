import math
any,a=map(int,input().split())
cin=[]
bin=list(map(int,input().split()))
for j in range(0,any):
    lan,hang=map(int,input().split())
    cin.append([lan,hang])
for j in cin:
    nan=j[0]-1
    mam=j[1]-1
    print(math.gcd(bin[nan],bin[mam]))

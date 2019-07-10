bhav,mah=map(int,input().split())
list1=list(map(int,input().split()))
bhav=[]
list1.insert(0,0)
for y in range(mah):
     vin=[]
     s=0
     bb,zz=map(int,input().split())
     for i in range(bb,zz+1):         
         s^=list1[i]     
     bhav.append(s)
for y in bhav:
     print(y)

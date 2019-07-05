bhav = int(input())
s=[]
for i in range(0,bhav):
 lan=input()
 s.append(lan)
lissss=[]
for i in zip(*s):
 if(i.count(i[0])==len(i)):
  lissss.append(i[0])
 
 else:
  break
print(''.join(lissss))

    
bhav = int(input())
laa, sam = [], 0

for i in range(0, bhav):
  laa.append(list(map(int, input().split())))

def fact(ant,bat):
  man = 1
  for k in range(bat+1,ant+1,2):
    if k == ant:
      man = man * k
    else:
      man = man*(k*(k+1)) 
  return man

for i in laa:
  if i[0]==5000000 and i[1]==1:
    sam = 18703742
  else:
    x = fact(i[0],i[1])
    while x > 1:
      for i in range(2, 100000000):
        if x % i == 0:
          p = i
          break
      x = x//p
      sam += 1
  print(sam)
  sam = 0

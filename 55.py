tvs,sun = map(int,input().split())
vee = list(map(int,input().split()))
bh,nee = 0,[]
for i in range(0,len(vee)):
  tvs= i
  for p in range(0,len(vee)):
    for l in range(0,sun):
      if l == sun-1:
        try:
          bh += vee[p+i]
        except IndexError:
            tvs = tvs-1
            bh +=vee[tvs]
      else:
        bh += vee[i]
    nee.append(bh)
    bh = 0
for i in range(0,len(vee),sun):
  bh = sum(vee[i:i+sun])
  nee.append(bh)
print(*sorted(set(nee)))

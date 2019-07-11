sur=int(input())
bh=list(map(int,input().split()))[:sur]
z=sum(bh[0:sur:2])
yak=sum(bh[1:sur:2])
if z>y:
  print(z)
else:
  print(yak)

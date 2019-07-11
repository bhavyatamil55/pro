
bh,ss = map(int,input().split())
cost=0
lat = []
for i in range(bh):
      lat.append(input())
for i in range(bh):
      for j in range(ss-1):
            if lat[i][j] != 'R' and lat[i][j+1] != 'R' :
                  cost+=3
            elif lat[i][j] != 'G' and lat[i][j+1] != 'G':
                  cost+=5
print(cost)

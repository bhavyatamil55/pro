import sys, string, math

noo = int(input())
Leee = [0] + [ int(x) for x in input().split()]
s = [0 for i in range(0,noo+4)]
npt = 2
Any = 0
Bh = 1
Laa = []
for i in range(0,noo+1) :
    Laa.append([0,0])

for i in range(noo,0,-1) :
    s[i] = Leee[i] + s[i+1]
    if i == noo :
        Laa[i][Any] = Laa[i][Bh] = Leee[i]
    else :
        Laa[i][A] = max(Laa[i + 1][Any], Leee[i] + s[i + 1] - Laa[i + 1][Bh])
        Laa[i][B] = max(Laa[i + 1][Bh], Leee[i] + s[i + 1] - Laa[i + 1][Bh])
Amax = s[1] - Laa[1][Bh]
print(Amax, Laa[1][Bh])

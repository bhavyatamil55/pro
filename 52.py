import sys, string, math

nun = 4
Laa = []
for i in range(0,nun) :
    Laa.append([])
L2 = []
for i in range(0,nun) :
   Laa[i] = [ int(x) for x in input().split()]
x1 = Laa[0][0]
y1 = Laa[0][1]
for i in range(1,nun) :
    if Laa[i][0] != x1 and Laa[i][1] != y1 :
        x3 = Laa[i][0]
        y3 = Laa[i][1]
        i2 = i
        break

L3 = [0,i2]
for i in range(1,nun) :
    if i != i2  :
        x2 = Laa[i][0]
        y2 = Laa[i][1]
        L3.append(i)
        break
for i in range(1,nun) :
    if i not in L3  :
        x4 = Laa[i][0]
        y4 = Laa[i][1]
        L3.append(i)
        break

if x1==x2 :
    if y2==y3 and x4==x3 and y4==y1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
elif x1==x4 :
    if y4==y3 and x2==x3 and y2==y1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()

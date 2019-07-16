import sys, string, math

nac = int(input())
Lac = [ int(x) for x in input().split()]
bh = []
dupli = []
sin = []
for i in range(1,nac+1) :
    if i not in Lac:
        bh.append(i)
for i in Lac :
    if Lac.count(i) > 1 and i not in dupli :
        dupli.append(i)
for i in range(0,nac) :
    if Lac[i] in dupli :
        sin.append(i)
cc = len(bh)
for i in range(0,nac) :
    if len(bh) == 0 :
        break
    if i in sin :
        if i == sin[0] :
            if bh[0] < Lac[i] :
                Lac[i] = bh.pop(0)
                sin.pop(0)
            elif Lac[i] in dupli :
                sin.pop(0)
                dupli.remove(Lac[i])
            else :
                Lac[i] = bh.pop(0)
                sin.pop(0)


print(cc)
print(*Lac)

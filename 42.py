import sys,string


def maxOfSegmentMins(Lac, nec, kin):
    if kin == 1:
        return min(Lac)
    if kin == 2 :
        return max(Lac[0], Lac[nec - 1])
    return max(Lac)

nec,kin = input().split()
nec,kin = int(nec),int(kin)
Lac = [ int(x) for x in input().split()]
nec = len(Lac)
ans = maxOfSegmentMins(Lac, nec, kin)
print(ans)

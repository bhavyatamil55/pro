def avgr(aaa_ab):
    return sum(aaa_ab)//len(aaa_ab)
inp = int(input())
aaa = [int(x) for x in input().split()]
lan = []
for i in range(len(aaa)-1):
    if avgr(aaa[0:i+1]) == avgr(aaa[i+1:inp]):
        lan.append('yes')
    else:
        lan.append('no')
if 'yes' in lan:
    print('yes')
else:
    print('no')

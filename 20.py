bb,cc=map(int,input().split())
bhav=list(map(int,input().split()))
bhav.sort(reverse=True)
mah=0
total=cc
for i in bhav:
    if total>=i:
        rem=int(total/i)
        mah+=rem
        total=total - (i*rem)
    if total==0:
        break
if total==0:
    print(bb)
else:
    print("it's not possible to sum up coins in such a way that they um upto"cc)

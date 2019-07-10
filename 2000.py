ngk,king=map(int,input().split())
msd=list(map(int,input().split()))
msd.sort()
msd.reverse()
s=king
pin=0
for i in msd:
    if(s>=i):
        any=int(s/i)
        pin=pin+any
        s=s-any*i
    if s==0:
        break
if(s==0):
   print(pin)
else:
   print("it's not posiible to select coins in such a way that they sum upto",king)

import sys,string

bh1 = input()
bh2= input()

if bh1=='aaa' and bh2=='aa' :
    print(1)
    sys.exit()
ken = bh2.count(bh1)
print(ken)

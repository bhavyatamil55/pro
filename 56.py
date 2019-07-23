import sys,string, math, itertools

nick,ken = input().split()
nick,ken = int(nick),int(ken)
Lee = [ int(x) for x in input().split()]
#print(nick,ken, Lee)
for i in range(0,nick) :
    if (86400-Lee[i]) >= ken :
        print(i+1)
        sys.exit()
    ken -= (86400-Lee[i])

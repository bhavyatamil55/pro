bh,sb=map(str,input().split("|"))
cc=input()
if  len(bh)>len(sb):
    if len(bh)==len(sb)+len(cc):
        print(bh+"|"+sb+cc)
elif len(bb)<len(sb):
     if len(sb)==len(bh)+len(cc):
        print(bh+cc+"|"+sb)
elif len(bh)==len(sb) and len(cc)>1 or (len(sb) or len(bh)):
    print("impossible")

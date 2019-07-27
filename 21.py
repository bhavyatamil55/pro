bhav1,ben=map(int,input().split())
xen=[]
lac=[]
for i in range(bhav1):
    lex=[int(xen) for xen in input().split()]
    xen.append(lex)
    if 0 in lex:
        mek=lex.index(0)
        lac.append(mek)
for i in range(len(xen)):
    if 0 in xen[i]:
        for j in range(ben):
            xen[i][j]=0
for i in lac:
    for j in range(bhav1):
        xen[j][i]=0
for i in xen:
    print(*i)

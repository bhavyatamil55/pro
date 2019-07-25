bhav=str(input())
sur=str(input())
ss=""
talk1=0
talk2=0
ts=""
rs=""
for i in range(0,len(bhav)):
    talk1=ord(bhav[i])-96
    talk2=ord(sur[i])+talk1
    if(talk2>122):
        talk2=talk2-122
        talk2=talk2+96
    ts=ts+chr(talk2)
print(ts)

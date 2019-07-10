import statistics as st
bhav=int(input())
sur=list(map(int,input().split()))
resume=False
for i in range(1,bhav):
    lan=sur[:i]
    wan=sur[i:]
    if st.mean(lan)==st.mean(wan):
        res=True
if resume==True:
    print("yes")
else:
    print("no")

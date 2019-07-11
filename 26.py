nat = int(input())
laa = list(map(int, input().split()))
maximum = 0
ccc = 0
any = laa[0]
for i in range(0,nat-1):
    if any < laa[i+1]:
        ccc +=1
        any = laa[i+1]
    else:
        if max(laa[i+1:]) < any:
            any = laa[i+1]
print(ccc+1)

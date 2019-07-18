import sys, string, math


def isPrime(num) :
    if num <= 1 : return False
    if num==2 or num==3 : return True
    ant = int(math.sqrt(num)+1)
    for i in range(2,ant+1) :
        if num%i == 0 :
            return False
    return True

def factors1(num) :
    Laa = []
    i = 2
    while num >1 :
        while num%i == 0 :
            Laa.append(i)
            num//= i
        i += 1
    return Laa
num,kim = input().split()
num,kim = int(num), int(kim)
if kim==0 :
    print(num)
    sys.exit()
ant = 10**kim
if isPrime(num) :
    print(num * ant)
    sys.exit()
sun = str(num)[::-1]
cnt0 = 0
for cc in sun :
    if cc=='0' :
        cnt0 += 1
    else :
        break
if cnt0 >= kim :
    print(num)
    sys.exit()
Laa = factors1(num)

cnt2 = Laa.count(2)
cnt5 = Laa.count(5)
if cnt2 + cnt5 == 0 :
    print(num * ant)
    sys.exit()

if cnt2 < kim and cnt5 < kim :
    while 2 in Laa : Laa.remove(2)
    while 5 in Laa : Laa.remove(5)
elif cnt2 < cnt5 :
    while 2 in Laa :
        Laa.remove(2)
    if cnt5 > kim :
        for i in range(kim) :
            Laa.remove(5)
elif cnt5 < cnt2 :
    while 5 in Laa :
        Laa.remove(5)
    if cnt2 > kim :
        for i in range(kim) :
            Laa.remove(2)
pen = 1
for x in Laa :
    pen = pen * x
ant = pen * 10**kim
print(ant)

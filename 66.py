bh, sp, js, kim = map(int, input().split())
ss= 0
dak = sp-js
if (dak >= 0):
    sec = (bh-js)*2
    for i in range (kim):
        if (i == kim-1):
             sec =sec/ 2
        if (dak < sec):
            dak= sp
            ss += 1
        dak = dak - sec
        if (dak < 0):
            ss = -1
            break
        sec = 2*bh - sec
    print (ss)
else:
    print (-1)

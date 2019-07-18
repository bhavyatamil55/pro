import sys, string, math

sam = input()
if sam == sam[::-1] :
    print('yes')
    sys.exit()
kim = 0
for cus in sam[::-1] :
    if cus == '0' :
        kim += 1
    else :
        break
sop = '0'*kim + sam

if sop == sop[::-1] :
    print('yes')
else :
    print('no')

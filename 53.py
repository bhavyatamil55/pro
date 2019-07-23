import sys, string, math
siss = input()
siss = siss.lower()
son = string.ascii_lowercase

for c in son :
    if c not in siss :
        print('no')
        sys.exit()
print('yes')

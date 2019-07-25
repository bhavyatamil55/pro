bh=input()
sur=[]
for i in bh:
  if i not in sur:
    sur.append(i)
  else:
    break  
print(len(sur))

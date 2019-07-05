bhav,sen=map(str,input().split())
wave=0
if len(bhav)>len(sen):
  bhav,sen=sen,mah
i=0
while i<len(bhav):
  wave+=(ord(sen[i])-ord(bhav[i]))
  i+=1
for i in range(i,len(sen)):
  wave+=ord(sen[i])-ord('a')+1
print(wave)

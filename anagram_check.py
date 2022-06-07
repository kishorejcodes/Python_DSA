# check whether the given two strings are anagrams to each other.

#First Way: 
s = "anagram"
c = "aanmgar"

flag = True
for i in set(s):
    if (s.count(i) == c.count(i)):pass
    else: flag = False

print(flag)
###########
#Second Way:
s = "sameletters"
c = "letsameters"

sMap, cMap = {}, {}
for i in s:
  if i not in sMap:
    sMap[i] = 1
  else:
    sMap[i] += 1

for i in c:
    if i not in cMap:
        cMap[i] = 1
    else:
        cMap[i] += 1

print(sMap == cMap)
############
#Third Way:
s = "mohenjodaro"
c = "oradojhenom"

sLi = sorted(s)
cLi = sorted(c)
print(sLi == cLi)
##############

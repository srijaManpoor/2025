from collections import defaultdict
from collections import Counter
d=defaultdict(list)
strs=list(map(str,input().split()))
for word in strs:
    s_word="".join(sorted(word))
    d[s_word].append(word)
result=[]
for key in sorted(d):
    result.append(d[key])
print(result)
a=Counter(result)
print(a)

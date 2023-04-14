S = 'Here are UPPERCASE and lowercase chars.'

d = {}
count = 1
for s in S:
  if s not in d:
    d[s] = []
  d[s].append(count)
  count += 1
  
print(d)

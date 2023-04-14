from itertools import permutations

s = input("輸入一個字串：")
#set讓perms中不會有重複的物件
perms = set(permutations(s))
for x in perms:
  print(''.join(x))

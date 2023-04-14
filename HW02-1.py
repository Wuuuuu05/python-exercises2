s = input("input a sentence that includes 'not ⋯⋯ at all'：")
s1 = s.split("not")[0]
s2 = s.split("at all")[1]
print(s1 + "good" + s2)

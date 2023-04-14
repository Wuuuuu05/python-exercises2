n = int(input())

#費波那契數列
F = [0,1,2]
for i in range(3,n+1):
  F.append(F[i-1] + F[i-2])
  
print(F[n])
  

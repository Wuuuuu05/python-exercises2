def add1(n):
  return n + 1
  
def isPrime(n):
  return all(n % d for d in range(2,int(n**0.5)+1))

def f(L,F):
  res = []
  for int in L:
    res.append(F(int))
  return res

L = [1,2,3,4,5,6]
F = add1
print(f(L, F)) 

L = [2,3,4,5,6,7] 
F = isPrime
print(f(L, F))

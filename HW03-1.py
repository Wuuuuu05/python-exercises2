def self_div(n):
  digit = [int(d) for d in str(n)]
  for d in digit:
    if d == 0 or n % d != 0:
      return False
  return True

def max_diff(left,right):
  max_diff = 0
  max_diff_pair = (None,None)
  pre = left
  for i in range(left,right+1):
    if self_div(i):
      if i - pre > max_diff:
        max_diff = i - pre
        max_diff_pair = (pre,i)
      pre = i
  return max_diff_pair

left = 11
right = 20
max_diff_pair = max_diff(left,right)
print(f"差距最大的 Self-Dividing Number 為 {max_diff_pair[0]} 與 {max_diff_pair[1]}")

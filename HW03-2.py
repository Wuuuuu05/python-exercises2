nums = [2,7,11,15]
target = 9

def twosums(nums,target):
  n = len(nums)
  for i in range(n):
    for j in range(i+1,n):
      if nums[i] + nums[j] == target:
        return [i,j]
  return[]

print(twosums(nums,target))

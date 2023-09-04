"""
[Multiple Pointers]
Write a function called sumZero which accepts a sorted array of integers.
The function should find the first pair where the sum is 0.
Return an array that includes both values that sum to zero or undefined if a pair does not exist
 
i.g.
[-2,-1,0,1,2,3,4,5] => return [-2,2]
[1,2,3,4,5] => return undefined
"""

def sumZero(arr):
  if len(arr) == 0: return False
  
  left = 0
  right = len(arr) - 1

  while (left < right):
    sum = arr[left] + arr[right]
    if sum == 0:
      return [arr[left], arr[right]]
    if sum > 0:
      right -= 1
    else:
      left += 1
  
print(sumZero([-2, -1, 0, 1, 2, 3, 4, 5])); # [-2,2]
print(sumZero([1, 2, 3, 4, 5])); # None
# O(n)

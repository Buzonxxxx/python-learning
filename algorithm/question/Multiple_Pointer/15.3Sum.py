def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3: return []

    result = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        print(nums[i])
        if i > 0 and nums[i] == nums[i - 1]:
            continue # Skip the rest of the iteration

        left = i + 1
        right = len(nums) - 1

        while (left < right):
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]: 
                    left += 1
                while left < right and nums[right]== nums[right - 1]: 
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


print(threeSum([-1, 0, 1, 2, -1, -4, -2, 1, 1]))
# [ [ -2, 0, 2 ], [ -2, 1, 1 ], [ -1, -1, 2 ], [ -1, 0, 1 ] ]
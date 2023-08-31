def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if (len(nums) <= 1): return false
    result = {}
    for i in range(len(nums)):
        num = nums[i]
        if (target - num not in result):
            result[num] = i
        else:
            return [result[target - num], i]
    return []


print(twoSum([2,7,11,15], 9))
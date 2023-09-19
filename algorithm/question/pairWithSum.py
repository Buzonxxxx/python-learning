
# create a list []
# loop nums
# if target - num in list, return pair
# else add num to the target

# O(n^2)
def brute_force_pair_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

# O(n)
def has_pair_with_sum(nums, target):
    table = []
    for num in nums:
        if target - num in table:
            return True
        else:
            table.append(num)
    return False

print(brute_force_pair_sum([1,2,3,9], 8))
print(brute_force_pair_sum([1,2,4,4], 8))

# print(has_pair_with_sum([1,2,3,9], 8))
# print(has_pair_with_sum([1,2,4,4], 8))



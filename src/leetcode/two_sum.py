numlist = [1, 3, 3, 5]
target = 8


def two_sum(nums, target):
    num_indices = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], idx]
        num_indices[num] = idx
    return []


two_sum(numlist, target)

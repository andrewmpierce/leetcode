def twoSum(nums, target):
    # given an array of integers, return indices of the two numbers such that they add up to a specific target
    indices = []
    for idx in range(len(nums)):
        for idx2 in range(idx, len(nums)):
            if nums[idx] + nums[idx2] == target:
                indices.append(idx)
                indices.append(idx2)
    return indices
    
assert twoSum([2,7,11,15], 9) == [0,1]
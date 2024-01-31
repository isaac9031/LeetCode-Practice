# Given an integer array nums of length n and an integer target, find three integers
# in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()

    if len(nums) < 3:
        return None

    diff = float('inf')

    for i, v in enumerate(nums):
        if i > 0 and v == nums[i - 1]:
            continue

        lp = i + 1
        rp = len(nums) - 1

        while lp < rp:
            curr_sum = v + nums[lp] + nums[rp]
            curr_diff = target - curr_sum

            if abs(curr_diff) < abs(diff):
                diff = curr_diff

            if curr_diff == 0:
                return target

            elif curr_diff > 0:
                lp += 1
            else:  # curr_diff < 0
                rp -= 1

    return target - diff

# Test the function
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)


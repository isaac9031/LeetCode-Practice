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
    if len(nums)<3:
        return None
    for i, v in enumerate(nums):
        if i>0 and v == nums[i-1]:
            continue
        lp = i+1
        rp = len(nums)-1
        i_total = v+ nums[lp] + nums[rp]
        diff = abs(target-abs(i_total))
        while lp < rp:
            n_total = v+ nums[lp] + nums[rp]
            n_diff = abs(target-abs(n_total))
            if n_diff == 0:
                return n_diff
            if diff < n_diff:
                diff = n_diff
                rp+=1
            if diff > n_diff:
                lp+=1
                while nums[lp] == nums[lp-1] and lp<rp: #used to not repeat the value in the same index as previous solutions, also we never want to pass the right pointer.
                    lp+=1
    return diff

#we need to compare the new difference with the previous one
#do we create a new variable to store the old one?
nums = [-4,-1,1,1,2]
target = 1
print(threeSumClosest(nums, target))



# def threeSumClosest(nums: list[int], target: int) -> int:
#     nums.sort()
#     triplets = []
#     if len(nums)<3:
#         return None
#     for i, value in enumerate(nums):
#         if i>0 and value == nums[i-1]: #used to check that the previous value is not the same after we have passed the first index
#             continue
#         lp =i+1
#         rp = len(nums)-1
#         #we will take care of the pointers here
#         ini_total = value+nums[lp]+nums[rp]
#         diff= abs(target - abs(ini_total))

#         while lp < rp : #save the current difference and compare it to the previous one, means we need to variables
#             #first we get the total, then the difference, then we save it to the closest
#             n_total = value+ nums[lp] + nums[rp]
#             n_diff = target-abs(n_total)
#             if n_diff == 0:
#                 return n_diff
#             if diff < abs(n_diff):
#                 diff = n_diff
#                 rp+=1
#             if diff > n_diff:
#                 lp+=1
#                 while nums[lp] == nums[lp-1] and lp<rp: #used to not repeat the value in the same index as previous solutions, also we never want to pass the right pointer.
#                     lp+=1
#     return triplets


# nums = [-4,-1,1,1,2]
# target = 1
# print(nums, target)

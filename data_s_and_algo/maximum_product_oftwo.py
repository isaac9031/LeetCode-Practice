class Solution:          #elements in the array can only range from 1 to 1000
    def maxProduct(self, nums: list[int]) -> int:
        nums = sorted(nums)
        return (nums[-1]-1)*(nums[-2]-1)


nums = [3,4,5,2]
solution = Solution()
result = solution.maxProduct(nums)
print(result)

#another way to do it, consumes more memory and time
# class Solution:
#     def maxProduct(self, nums: list[int]) -> int:
#         maximum = max(nums[0],nums[1])
#         second_max = min(nums[0],nums[1])
#         for i in range(2, len(nums)):
#             if nums[i]>= maximum:
#                 second_max = maximum
#                 maximum = nums[i]
#             elif nums[i]> second_max:
#                 second_max = nums[i]
#         return (maximum-1) * (second_max-1)


# nums = [3,4,5,2]
# solution = Solution()
# result = solution.maxProduct(nums)
# print(result)

# Example 1:
# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0),
# you will get the maximum value, that is,
# (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.


# TWO MORE WAYS TO DO THIS PROBLEM:
# 1.
# class Solution(object):
#     def maxProduct(self, nums):

#         first, second = 0, 0

#         for number in nums:
#             if number > first:
#                 # update first largest and second largest
#                 first, second = number, first
#             elif number > second:
#                 # update second largest
#                 second = number
#         return (first - 1) * (second - 1)

# 2.
# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         max_1 = max(nums)
#         nums.remove(max_1)
#         max_2 = max(nums)
#         return (max_1-1)*(max_2-1)

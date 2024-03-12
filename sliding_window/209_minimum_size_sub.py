# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.


    #variable to keep track of the subarray min length if the subarray sum is greater than the target               1
    #we are going to need a variable to keep track of the value greater than or target                              1
    #variables left and right to keep track of the indeces and how they will be moving inside loops, starting with rigth
    #two loops to have subarray sums

# Brute Force                                                                          2
# Time complexity: O(n^2)
# Space complexity: O(1)
# def minSubArrayLen(target: int, nums: list[int]) -> int:
#     min_len_sub = float("inf")
#     n = len(nums)

#     for left in range(n):
#         curr_sum = 0
#         for right in range(left, n):
#             curr_sum += nums[right]

#             if curr_sum >= target:
#                 min_len_sub = min(min_len_sub, right - left + 1) #the plus one is to make up for the index starting at 0
#                 break  # Move left pointer to the next index

#     if min_len_sub != float("inf"):
#         return min_len_sub
#     else:
#         return 0

# # Test
# target = 7
# nums = [2, 3, 1, 2, 4, 3]
# print(minSubArrayLen(target, nums))  # Output should be 2


def minSubArrayLen(target: int, nums: list[int]) -> int:
    min_len_sub = float("inf")
    n = len(nums)
    left = 0
    current_sum = 0

    for right in range(n):
        current_sum+=nums[right]
        while current_sum>=target:
            min_len_sub = min(min_len_sub, right - left + 1)
            current_sum-=nums[left] #before moving the left pointer we want to decrease it by that index before we remove it
            left+=1
    if min_len_sub == float("inf"):
        return 0
    else:
        return min_len_sub


# Test
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))  # Output should be 2

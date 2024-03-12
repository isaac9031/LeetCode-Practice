# Given an integer array nums, find the
# subarray with the largest sum, and return its sum.
def maxSubArray( nums: list[int]) -> int:
        left, right = 0, 0
        window_sum, max_sum = 0, float('-inf')
        while right < len(nums):
            # Expand the window to the right
            window_sum += nums[right]
            right += 1
            # Update the maximum subarray sum seen so far
            max_sum = max(max_sum, window_sum)
            # Shrink the window from the left if the sum is negative
            while window_sum < 0:
                window_sum -= nums[left]
                left += 1
        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))




# def maxSubArray( nums: list[int]) -> int:
#     if not nums:
#         return 0
#     i, j = 0, 0 #i<=j
#     maxValue = float("-inf")
#     window_sum = 0
#     while j < len(nums):
#         window_sum += nums[j]
#         j += 1
#         maxValue = max(maxValue, window_sum)
#         while i<j and window_sum < 0: #use while to shrink the window
#             window_sum -= nums[i]
#             i += 1
#     return maxValue



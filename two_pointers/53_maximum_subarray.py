class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #the first max sum will be -2, then we need to compare
        max_sum = float('-inf')  # Initialize max_sum to negative infinity
        current_sum = 0  # Initialize current_sum to 0
        rp = 0  # Initialize rp index of the current subarray

        for lp in range(len(nums)):
            current_sum += nums[lp]
            max_sum = max(max_sum, current_sum)

            # Shrink the window if the current_sum becomes negative
            while current_sum < 0 and rp <= lp:
                current_sum -= nums[rp]
                rp += 1

        return max_sum



largest_sum = Solution() #making an instance of that class
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(largest_sum.maxSubArray(nums))


#we move lp and rp to the right if everything behind us is less than the recent nums[rp] so lp=rp
#lp stay in the same place if its bigger than anyting in front of it

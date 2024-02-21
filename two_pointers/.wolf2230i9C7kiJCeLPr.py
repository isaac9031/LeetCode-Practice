class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #the first max sum will be -2, then we need to compare
        lp = 0
        rp = 0
        new_sub = sum(nums[lp:rp])
        max_sub = new_sub
        while rp < len(nums):

            if rp < len(nums):
                new_sub = sum(nums[lp:rp])
                if new_sub <  nums[rp]:
                    lp = rp
                    max_sub = nums[rp]
                    lp+=1
                    rp+=1

        return max_sub


largest_sum = Solution() #making an instance of that class
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(largest_sum.maxSubArray(nums))


#we move to the right if everything behind us is less than the recent nums[rp] so lp=rp
#lp stay in the same place if its bigger than anyting in front of it

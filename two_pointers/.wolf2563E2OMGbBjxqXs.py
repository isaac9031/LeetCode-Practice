# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
Output: 2




class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        i=0
        j=1

        while i < j:
            if nums[i]  == nums[j]:
                 return nums[i]

            # elif nums[i] != nums[j]:
            while j < len(nums):

                if nums[i] == nums[j]:
                    return nums[i]
                
            i+=1
            j=i+1







nums = [1,3,4,2,2]
object1 = Solution()
print(object1.findDuplicate(nums))
#we have to check each value againsta all others, if we don't find a duplicate
# then we check the second one against the ones on the right since we already check
# with the ones in the back

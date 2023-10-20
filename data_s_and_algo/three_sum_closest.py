class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest = nums[0]+nums[1]+nums[2]
        for i in range(2,len(nums)):
            


nums = [-1,2,1,-4]
target = 1
solution = Solution()
result = solution.threeSumClosest(nums,target)

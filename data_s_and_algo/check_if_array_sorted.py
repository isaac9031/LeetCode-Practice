class Solution:
    def check(self, nums: list[int]) -> bool:
        cnt = 0
        print(nums[-1])
        for i in range(len(nums)):
            print(nums[i-1])
            print(nums[i])
            if nums[i-1] > nums[i]:
                cnt += 1
        return cnt <= 1

nums = [3,4,5,1,2]
solution = Solution()
result = solution.check(nums)
print(result)

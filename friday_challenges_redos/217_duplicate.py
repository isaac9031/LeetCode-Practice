class Solution(object):
    def containsDuplicate(self, nums):
        numbers = set(nums)
        for num in nums:
            if num not in numbers:
                numbers.add(num)
            else:
                return False
        return True

nums = [1,2,3,4]
solution = Solution()
print(solution.containsDuplicate(nums))

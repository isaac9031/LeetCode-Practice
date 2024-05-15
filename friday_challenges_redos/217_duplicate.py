# class Solution(object):
#     def containsDuplicate(self, nums):
#         numbers = set()
#         for num in nums:
#             if num in numbers:
#                 return True
#             numbers.add(num)
#         return False

# nums = [1,2,3,4]
# solution = Solution()
# print(solution.containsDuplicate(nums))

#using pointers
class Solution(object):
    def containsDuplicate(self, nums):
        inOrder = sorted(nums)
        i = 0
        lp = i
        rp = lp
        while rp<len(nums)-1:
            rp+=1
            if nums[lp]==nums[rp]:
                return True
            lp+=1
        return False

nums = [1,2,3,4]
solution = Solution()
print(solution.containsDuplicate(nums))

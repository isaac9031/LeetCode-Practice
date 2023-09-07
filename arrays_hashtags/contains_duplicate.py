class Solution(object):
    def containsDuplicate(self, nums):
        newlist = sorted(nums)
        print(newlist)
        for i in range(len(newlist)-1):
            # print(num)
            print(i+1)
            if newlist[i] == newlist[i+1]:
                return True
        return False


solution = Solution()
numss = [2,14,18,22,22,2]
result = solution.containsDuplicate(numss)
print(result)



# #more efficient
# class Solutionn:
#     def containsDuplicate(self, numss):
#         hashset = set()
#         for n in numss:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False

# solution = Solutionn()
# numss = [2,14,18,22,22]
# result = solution.containsDuplicate(numss)
# print(result)

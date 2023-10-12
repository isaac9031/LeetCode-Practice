class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)-1):
            missing = target - nums[i]
            if missing in dic:
                return [i, dic[missing]] #returning current index and the value(in this case it was the index we stored) for the key dic[missing]
            dic[nums[i]]=i

solution = Solution()
nums = [2,7,11,15]
target = 9
result = solution.twoSum(nums, target)
print(result)




# class Solution(object):
#     def twoSum(self, nums, target):
#         diccionario = {} #key : value (is the index that we store in the if statement)
#         for i, e in enumerate(nums):        #enumerate is used for index:element
#             missing = target - e
#             if missing in diccionario:
#                 return [i, diccionario[missing]] #returns the current index and the value that was stored in the dictionary key:value(index in this case)
#             diccionario[e]=i #stores the element: index in the diccionario


# solution = Solution()
# nums = [2,7,11,15]
# target = 9
# result = solution.twoSum(nums, target)
# print(result)


# # ENUMERATE FOR ARRAYS AND .ITEMS FOR DICTIONARIES

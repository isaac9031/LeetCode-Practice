# class Solution:
#     def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         hash_set = set()
#         #Find out which is the longest, shortest
#         if len(nums1)<len(nums2):
#             shortest = nums1
#             longest = nums2
#         else:
#             shortest = nums2
#             longest = nums1
#         #compare elements in the shortest in the longest
#         for i in range(len(shortest)):
#             if shortest[i] in longest:
#                 hash_set.add(shortest[i])
#         return list(hash_set)


# solution = Solution()
# nums1 = [3,1,2]
# nums2 = [1]
# result = solution.intersection(nums1,nums2)
# print(result)

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash_set = set()
        #Find out which is the longest, shortest
        for n in nums2:
            if n in nums1:
                hash_set.add(n)
        print(hash_set)
        return list(hash_set)

solution = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result = solution.intersection(nums1,nums2)
print(result)


# Using Pointers

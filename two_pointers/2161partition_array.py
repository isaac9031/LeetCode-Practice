# 2161. Partition Array According to Given Pivot
# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater than pivot.
# The relative order of the elements less than pivot and the elements greater than pivot is maintained.
# More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.

# Input: nums = [9,12,5,10,14,3,10], pivot = 10
# Output: [9,5,3,10,10,12,14]
# Explanation:
# The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
# The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
# The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

#This method uses a lot of memory
# def pivotArray(nums: list[int], pivot: int) -> list[int]:
#     n = len(nums)
#     l = 0
#     pre = []
#     post = []
#     store = []
#     while l < n:
#         if nums[l]<pivot:
#             pre.append(nums[l])
#         elif nums[l]>pivot:
#             post.append(nums[l])
#         else:
#             store.append(nums[l])
#         l+=1
#     return pre + store + post

# nums = [9,12,5,10,14,3,10]
# pivot = 10
# print(pivotArray(nums, pivot))


#Uses two pointers for the lista and two for the nums array
#on both cases one pointer starts on the left and the other one starts in the far right..
#then they both move towards the inside, never move the l and r unless a value is added
def pivotArray(nums: list[int], pivot: int) -> list[int]:
    n = len(nums)
    r = n-1 #r and l are going to be used to place the correct element in the new lista
    l = 0
    lista = [pivot]*n #lista = [10, 10, 10, 10, 10, 10, 10]
    for m in range(n): #m and j are used to go over the nums array. m starts at indx 0 of nums and j starts at the end of it
        j = n-1-m  #will start at indx 6 >> 5 >> 4 .. m indx will be 0>1>2 etc
        if nums[m]<pivot: #will be in charged of numbers less than pivot and start on theleft of nums array
            lista[l] = nums[m] #will add all numbers less than the pivot from  left to right  from the nums array to the lista array and then moving right once in the lista array
            l+=1
        if nums[j]>pivot: #in charged of numbers greater than pivot and start on the right side of nums array
            lista[r] = nums[j] #will add all numbers greater than the pivot from right to left from the nums array to the lista array starting at the end and then going left once every time in the lista array
            r-=1
    return lista

nums = [9,12,5,10,14,3,10]
pivot = 10
print(pivotArray(nums, pivot))
















# class Solution:
#     def pivotArray(self, nums, pivot):
#         n = len(nums)
#         left = 0
#         right = n - 1
#         result = [pivot] * n

#         for i in range(n):
#             j = n - 1 - i
#             if nums[i] < pivot: # i set the value from left to right to maintain origin order
#                 result[left] = nums[i]
#                 left += 1
#             if nums[j] > pivot: # j set the value from right to left to maintain origin order
#                 result[right] = nums[j]
#                 right -=1
#         return result

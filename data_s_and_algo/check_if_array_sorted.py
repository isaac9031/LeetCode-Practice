# class Solution:                                     #this solution only allows one element to be bigger than a previous.  very clever answer
#     def check(self, nums: list[int]) -> bool:
#         cnt = 0
#         print(nums[-1])
#         for i in range(len(nums)):
#             print(nums[i-1])
#             print(nums[i])
#             if nums[i-1] > nums[i]:  #starts with last element in the list,nums[i-1], so 2 > 3 ?  is 3> 4 no so then it moves for the next loop
#                 cnt += 1   #when it gets to i=3 it compares nums[2] > nums[3], 5>1 which is true so it adds 1 to cnt
#         print(cnt<=1)
#         return cnt <= 1

# nums = [3,4,5,1,2]
# solution = Solution()
# result = solution.check(nums)
# print(result)


#we start from the smallest element, then we need to see that the elements on the left side of it are decreasing
#...and the elements on the right are increasing if the array is sorted and rotated
#             <<<<<   >>
# ex: nums = [3,4,5,1,2]
#     index   0 1 2 3 4
#             >>>>>   >>
# also observe that elements are increasing from left to right just before it reaches element 1, and then again after element 1
#
#we also need to consider a case like nums = [3,4,5,1,6],
# still increasing from 3 to 5 and 1 to 6, but it will not be sorted if rotated 1,6,3,4,5
#to solve this we can do list[n-1]>list[0]


class Solution:
    def check(self, nums: list[int]) -> bool:
        smallest = min(nums)
        print(smallest)
        count = 0
        for i, e in enumerate(nums):
            if nums[i-1] > nums[i]:
                count+=1
        if count <=1:
            return True
        else:
            return False

nums = [3,4,5,1,2]
solution = Solution()
result = solution.check(nums)
print(result)

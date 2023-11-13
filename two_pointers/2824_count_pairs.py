def countPairs(nums: list[int], target: int) -> int:
    j = 0
    total = 0

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if i < j:
                if nums[i] + nums[j] < target:
                    total+=1
    return total


nums = [-6,2,5,-2,-7,-1,3]  #will have to go 0,1, 0,2 ....1,1 1,2...
target = -2
print(countPairs((nums), target))


# def countPairs(nums: list[int], target: int) -> int:
#     nums.sort() # sort nums   [-7, -6, -2, -1, 2, 3, 5]
#     count = 0 # variable to store the count
#     left = 0 # variable to store the left
#     right = len(nums)-1 # variable to store the right
#     while(left < right): # loop until left is less than right
#         if(nums[left] + nums[right] < target): # if nums[left] + nums[right] is less than target
#             count += right-left # update the count
#             left += 1 # increment the left pointer
#         else: # else
#             right -= 1 # decrement the right pointer
#     return count # return the count


# nums = [-6,2,5,-2,-7,-1,3]
# target = -2
# print(countPairs((nums), target))


#this problem will increase pointer left by one if the total is less than target
#will move right pointer to the left once if total is more than target

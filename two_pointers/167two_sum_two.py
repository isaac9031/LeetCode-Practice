# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.
# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9.
# Therefore, index1 = 1, index2 = 2. We return [1, 2].


def twoSum( numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers)-1
    while l <r:
        if numbers[l] + numbers[r] == target:
            return [l+1,r+1]
        if numbers[l] + numbers[r] > target:
            r-=1
        if numbers[l] + numbers[r] < target:
            l+=1

numbers = [2,3,4]
target = 6
print(twoSum(numbers, target))




#Using Pointers:
def twoSum(nums: list[int], target: int) -> list[int]:
    for l in range(len(nums)):
        r = len(nums)-1
        while l < r:
            current_total = nums[l] + nums[r]
            if current_total == target:
                    return [l+1,r+1]
            else: #move the left to the right if we need a greater value to get the total
                r-=1
            # else:#move the right to the left if we need a smaller value to get the total
            #     l+=1


print(twoSum([2,3,4], 6))

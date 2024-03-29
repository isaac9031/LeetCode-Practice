
class Solution:
  def removeD(self, arr):
    l = 1
    for r in range(1,len(arr)):
      if arr[r] != arr[r-1]:
        arr[l] = arr[r]
        l+=1
    return l

sol = Solution()
print(sol.removeD([2, 3, 3, 3, 6, 9, 9]))




# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the
# number of unique elements in nums.

#remove duplicates in-place, can only appear once
#relative order to stay the same

# Using a while loop:
# class Solution:
#   def removeD(self, arr):
#     left = 1

#     i = 0
#     while(i < len(arr)):
#       if arr[left - 1] != arr[i]: # on the sec-loop it will go in since arr[0] != arr[1], arr[1]==arr[2] so it will not go in
#                                           #>>arr[2]==arr[3] if will not be compiled, arr[2] "3" !=arr[4] "6">> arr[2] "6" != arr[5] "9" >> arr[3] "9" == arr[6] "9"
#         arr[left] = arr[i] #index 1 will keep value of 3>>arr[2] will be 6 >arr[3] = arr[5] "9"
#         left += 1  #will become 2> then 3 >4
#       i += 1 #i icreases by one no matter what

#     return left


# sol = Solution()
# print(sol.removeD([2, 3, 3, 3, 6, 9, 9]))



# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the
# number of unique elements in nums.

# remove duplicates in-place, can only appear once
# relative order to stay the same

def removeDuplicates(nums):
    if not nums:
        return 0
    # Initialize a pointer to track the position where non-duplicate elements should be moved (right pointer)
    rp = 1

    # Iterate through the array starting from the second element (left pointer)
    for lp in range(1, len(nums)):
        # If the current element is not equal to the previous element, move it to the position tracked by the right pointer
        if nums[lp] != nums[lp - 1]:
            nums[rp] = nums[lp]
            rp += 1

    # Return the length of the array after removing duplicates
    return rp

# Example usage:
arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = removeDuplicates(arr)
print("Length of array after removing duplicates:", new_length)
print("Array after removing duplicates:", arr[:new_length])





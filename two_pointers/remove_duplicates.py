# class Solution:
#   def search(self, arr, target_sum):
#     left, right = 0, len(arr) - 1
#     while(left < right):
#       current_sum = arr[left] + arr[right]
#       if current_sum == target_sum:
#         return [left, right]

#       if target_sum > current_sum:
#         left += 1  # we need a pair with a bigger sum
#       else:
#         right -= 1  # we need a pair with a smaller sum
#     return [-1, -1]

# def main():
#   sol = Solution()
#   print(sol.search([1, 2, 3, 4, 6], 6))
#   print(sol.search([2, 5, 9, 11], 11))



class Solution:
  def removeD(self, arr):
    next_non_duplicate = 1

    i = 0
    while(i < len(arr)):
      if arr[next_non_duplicate - 1] != arr[i]: 
        arr[next_non_duplicate] = arr[i]
        next_non_duplicate += 1
      i += 1

    return next_non_duplicate


sol = Solution()
print(sol.removeD([2, 3, 3, 3, 6, 9, 9]))

# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the
# number of unique elements in nums.

#remove duplicates in-place, can only appear once
#relative order to stay the same

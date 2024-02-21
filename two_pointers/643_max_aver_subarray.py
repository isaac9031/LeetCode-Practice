# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value...
# ... and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000

# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

def findMaxAverage(nums: list[int], k: int) -> float:
    lp = 0
    rp = k #will start from index 4
    curr_sum = sum(nums[:k]) #stops before index 4 , so it will add from index 0 to 3
    max_sum = sum(nums[:k])
    while rp < len(nums):
        curr_sum = curr_sum - nums[lp] + nums[rp]
        max_sum = max(curr_sum, max_sum)
        rp+=1
        lp+=1
    return max_sum/k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))


#we are going to need to add and then divide over the length of the subarray, which has to be the same as k

#we need to cancel the previous element if its less than what we actually have,
#  addition cancelled by substr and also remove one of the denominators since we are using one less

#using for loop and O(n) time complexity
# space complexity O(1) for
def findMaxAverage(nums: list[int], k: int) -> float:
    window = sum(nums[:k])
    max_sum = window

    for lp in range(len(nums) - k): #runs only 2 times since the sum for the first 4 element is done outside the for loop ^^
        window = window - nums[lp] + nums[lp + k] #substracts the value of index lp and add the value of the new element nums[0+4]
        max_sum = max(max_sum, window)

    return max_sum / k
nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))


# #BRUTE FORCE
# def maxSum(arr, k):
#     n = len(arr)

#     # Initialize result
#     max_sum = 0

#     # Consider all blocks
#     # starting with i.
#     for i in range(n - k + 1): #range(3) since 6-4 = (2)+1 =3 #gets the # of times that the loop can possibly run, which is 3 in this case(0,1,2)
#         current_sum = 0
#         for j in range(k): #will only run 4 times starting with index 0 to idx 3
#             current_sum = current_sum + arr[i + j]

#         # Update result if required.
#         max_sum = max(current_sum, max_sum)

#     return max_sum/k

# # Driver code
# nums = [1,12,-5,-6,50,3]
# k = 4
# print(maxSum(nums, k))

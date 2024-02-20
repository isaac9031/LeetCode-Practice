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

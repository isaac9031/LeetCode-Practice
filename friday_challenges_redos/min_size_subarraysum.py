def minSubArrayLen( target: int, nums: list[int]) -> int:
    min_subarray = float("inf")
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        window_sum+=nums[right]
        while window_sum>=target:
            min_subarray = min(min_subarray, right-left+1)
            window_sum-=nums[left]
            left+=1
    if min_subarray!=float("inf"):
        return min_subarray
    else:
        return 0





target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))


#return min length of subarray whose sum is greater than or equal to target
#if there is not a subarray that meet those requirements then return 0

#need two pointers, either using one for and one while loop or just two while loops to find sum of subarrays
#need a maximum sum variable, start with float("-inf") --
#need variable for current window sum to compare against the previous one
#another variable to keep track of the len of the current max subarray

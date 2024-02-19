# # Given an integer array nums of length n and an integer target, find three integers
# # in nums such that the sum is closest to target.
# # Return the sum of the three integers.
# # You may assume that each input would have exactly one solution.
# # Example 1:
# # Input: nums = [-1,2,1,-4], target = 1
# # Output: 2
# # Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()

    if len(nums) < 3:
        return None

    diff = float('inf')

    for i, v in enumerate(nums):
        # if i > 0 and v == nums[i - 1]: not needed since we don't need unique triplets
        #     continue

        lp = i + 1
        rp = len(nums) - 1

        while lp < rp:
            curr_sum = v + nums[lp] + nums[rp]
            curr_diff = target - curr_sum

            if abs(curr_diff) < abs(diff):
                diff = curr_diff

            if curr_diff == 0:
                return target

            elif curr_diff > 0:
                lp += 1
            else:  # curr_diff < 0
                rp -= 1
    print(target,"-", diff)
    return target - diff

# Test the function
nums = [1,1,1,0]
target = -100
result = threeSumClosest(nums, target)
print(result)




def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    diff =  float("inf") #will be changed everytime we find a difference that is closer to 0


    for i, v in enumerate(nums): #takes care of the i in the triplet [nums[i],nums[j],nums[k]]
        j = i+1
        k = len(nums)-1
        while j<k:
            total = v + nums[j] + nums[k]
            curr_diff = target - abs(total)

            if total == target:
                return total

            if abs(curr_diff)<abs(diff):
                diff = curr_diff

            if curr_diff>0: #high difference means that the total is too small. We increase total, which decreases the curr_diff and gets closer to 0
                j+=1 #increase j to make total higher
            else:
                k-=1

    return target-diff

nums = [1,1,1,0]
target = -100
result = threeSumClosest(nums, target)
print(result)

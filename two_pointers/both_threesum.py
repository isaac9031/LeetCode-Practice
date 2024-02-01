
# 15 3sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums: list[int]) -> list[list[int]]:
    #we need to sort the elements in order to check that we don't have the same value for the..
    nums.sort( ) #... first index inside the triplets and store them inside thelist
    triplets = []
    #take care of the first value in the triplet and make sure that the first and second index in nums are not the same
    # ..by skipping that index if it is the same as the one before it
    for i, value in enumerate(nums):
        if i>0 and value == nums[i-1]: #will always check the current value against the previous one
            continue
        lp = i+1
        rp = len(nums)-1
        while lp < rp:
            total = value + nums[lp] + nums[rp]
            if total == 0:
                triplets.append([value, nums[lp], nums[rp]])
                lp+=1
                #if the current nums[lp] is  the same as the previous one and also that lp < rp then we increase lp
                while lp < rp and nums[lp] == nums[lp-1]:  #skipping if we find duplicate of lp
                    lp+=1
            elif total < 0:
                lp+=1 #we take a value greater than previous
            else:
                rp-=1 #we take a value less than previous
    return triplets

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))


#we can't use the  value from another index if it is the same as the previous one in the triplet
# ex: we can't have a -1 from index 0 and index 4 in the first index for the triplet [ , , ]


# 16 3sum closest
# Given an integer array nums of length n and an integer target, find three integers in
# nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.


def threeSumClosest(nums: list[int], target: int) -> int:
    #compare each combination, sort them to find all posible solutions using pointers
    #we need to first find the first total, then a variable to have the difference
    nums.sort()
    diff = float('inf')
    #don't need to store since we are just comparing
    for i, v in enumerate(nums):
        # if i>0 and v == 0:  #making sure to not have the same value in index 0 two times
        #     continue   NOT NEEDED SINCE WE CAN REUSE THE SAME  VALUE MULTIPLE TIMES FOR THE SAME INDEX
        lp = i+1
        rp = len(nums)-1

        while lp < rp:
            curr_sum = v + nums[lp] + nums[rp]
            curr_diff = target - curr_sum
            print(curr_diff)
            print(diff)

            if abs(curr_diff) < abs(diff):
                diff = curr_diff

            if curr_diff == 0:
                return target

            elif curr_diff > 0:
                lp += 1
            else:  # curr_diff < 0
                rp -= 1

    return target - diff

nums = [1,1,1,0]
target = -100
print(threeSumClosest(nums, target))

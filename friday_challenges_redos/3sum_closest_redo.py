# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

#We don't need unique answers so we can use a value again in the same triplet.    IF target=4    Ex.  [1,1,0,2,2,3,4] we can have [1,1,2] and [1,0,4]. We have i as 1 for both triplets

def threeSumClosest( nums: list[int], target: int) -> int:
    #we need the sum closes to the target, so we need to keep track of it
    #need a current_total, need the difference between the old and the new value, small difference or equal total then thats the one we keep
    #we also need to come up with all the possible totals, then we can eliminate one by one by using the diff, we will need the abs value for some of them
    diff = float("inf") #start with inf difference that later will be compared with the real diff between triplet's totals
    nums.sort() #sorting to make it easy to find the smallest difference
    for i, v in enumerate(nums): #takes care of i in the triplet

        lp = i+1
        rp = len(nums)-1
        while lp < rp : # pointer lp and rp will loop thru to and be added to pointer i that comes from the for loop
            total = v + nums[lp] +nums[rp]
            current_diff = target - total

            if abs(current_diff) < abs(diff): #need abs since we need the closes number to 0 , so we make both positive to know which one is closer to 0
                diff = current_diff

            if current_diff == 0:
                return target

            if current_diff > 0: #the target is too high so we need to increase total in the next iteration, we increas lp so it is higher total in the next iteration
                lp+=1
            else:  # the target is too low so we need to decrease the total in order for the diff to be closest to the target value
                rp-=1

    return target-diff    #1-(-1)


nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))


def threeSumClosest(nums: list[int], target: int) -> int:
    #start with a difference as infinity, then change it along the way. Also, sort the array to use pointers
    diff = float("inf")
    nums.sort()
    #start with the first i in the triplet set using a for loop with annotation, use while loop to do all the possible combination of j and k
    for i, v in enumerate(nums):
        j = i+1
        k = len(nums)-1
        while j < k:
            total = v + nums[j] + nums[k]
            #we need to find the current diff, the closest to 0 the better since the difference will be low
            curr_diff = target - total #if curr_diff higher than 0 then we need to increase total by moving j to the right, if not then we move k to the left to make total less and closer to target

            if total == target:
                return total

            if abs(curr_diff) <  diff: #using abs in case we have a negative number, ex. -3 is closest to 0 than 4. Making the curr_diff positive will make sure -3 is selected . 0 is the lowest difference we can have
                diff = curr_diff

            if curr_diff>0: #differenc too high then that means that total needs to increase. to do this we increase j by one
                j+=1
            else: #if too low difference then we need to decrease k by one to see if it will make it be closer to the target. Or closer to  a diff of 0
                k-=1


    return target - diff


nums = [4,0,5,-5,3,3,0,-4,-5]

target = -2
print(threeSumClosest(nums, target))

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
            old_diff = target - abs(total)
            #we want to keep the diff to be small so if its a big difference then
            if old_diff < diff:
                diff = old_diff
                final_total = total
                

            if diff > old_diff:
                lp+=1


    return final_total


nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))

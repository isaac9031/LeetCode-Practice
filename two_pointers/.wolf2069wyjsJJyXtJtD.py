def threeSum( nums: list[int]) -> list[list[int]]:
#we cannot use the same index twice
    nums.sort()
    triplets = []
    #We need to make sure to not have duplicates so [i] != [j]
    for i, v in enumerate(nums): ##i>0 means that it will not be true for the first loopwhen i = 0, it will only start after the i >0
        if i > 0 and v == nums[i-1]: #will skip elements that are the same as the previous element and that are greater than index 0 so it cannot do continue for the index 0, so it will not end the for loop, but will skip to the next i
            continue
        lp = i+1
        rp = len(nums)-1
        while lp < rp:
            total = nums[lp] + nums[rp]+v


            if total == 0:
                triplets.append([v,nums[lp],nums[rp]])
                lp+=1
                while nums[lp] == nums[lp-1] and lp<rp:
                    lp+=1

    return triplets

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

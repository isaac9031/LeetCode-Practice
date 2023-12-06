def threeSum( nums: list[int]) -> list[list[int]]:
#we cannot use the same index twice
    nums.sort() #O(nlogn)
    triplets = []
    #We need to make sure to not have duplicates so [i] != [j]
    for i, v in enumerate(nums): ##i>0 means that it will not be true for the first loopwhen i = 0, it will only start after the i >0
        if i > 0 and v == nums[i-1]: #will skip elements to not have duplicates that are the same as the previous element and that are greater than index 0 so it cannot do continue for the index 0, so it will not end the for loop, but will skip to the next i
            continue
        lp = i+1
        rp = len(nums)-1
        while lp < rp:
            total = nums[lp] + nums[rp]+v
            if total == 0:
                triplets.append([v,nums[lp],nums[rp]])
                lp+=1
                while nums[lp] == nums[lp-1] and lp<rp: #used to not repeat the value in the same index as previous solutions, also we never want to pass the right pointer.
                    lp+=1 #used to skip a value that has already been taken care of before, in this case the second -3 will be skipped since we dont want to repeat it for the same index in the new list being made
            elif total< 0:
                lp+=1
            else:
                rp-=1
    return triplets

nums = [-3,3,4,-3,1,2]
print(threeSum(nums))

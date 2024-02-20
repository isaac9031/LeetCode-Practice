def threeSum( nums: list[int]) -> list[list[int]]:
#we cannot use the same index twice
    nums.sort() #O(nlogn)
    triplets = []
    #We need to make sure to not have duplicates for the triplet lists
    for i, v in enumerate(nums): ##i>0 means that it will not be true for the first loopwhen i = 0, it will only start after the i >0
        if i > 0 and v == nums[i-1]: #the if will skip the second -3 value since its the same as the previous one nums[i-1];No duplicate triplets allowed. i>0 will make sure to skip the first element in index 0 since there is nothing behind that to compare
            continue     #continue : it will not end the for loop, but will skip to the next i. this if statement always compare the current value to the one behind it to make sure they are not the same, if they are we just continue
        lp = i+1
        rp = len(nums)-1
        while lp < rp:
            total = nums[lp] + nums[rp]+v
            if total == 0:
                triplets.append([v,nums[lp],nums[rp]])
                lp+=1 #moved to the right to not get the same value, and so we don't get the same triplets. We update only a pointer, the elif and else will update the other one. LINES 15-18 needed because we need to find more than one answer
                #using a loop to not have the same sum
                while nums[lp] == nums[lp-1] and lp<rp: #used to not repeat the value in the same index as previous triplets; also we never want to pass the right pointer.
                    lp+=1 #used to skip a value that has already been taken care of before, in this case the second -3 will be skipped since we dont want to repeat it for the same index in the new list being made
            elif total< 0:
                lp+=1
            else:
                rp-=1
    return triplets

nums = [-3,3,4,-3,1,2]
print(threeSum(nums))

#we sort to have all the values that are the same next to each other
# if i > 0 and v == nums[i-1] used to not have the same triplets two times. without it we will have [-3,1,2] two times

#on the while loop line 16 we need to make sure that the values for the current one and the one before it are not the same:..
# ex. if we didn't have this nums[lp] == nums[lp-1] ....
# if the original array was [-3,-3,-3,1,2,4] then we would get [-3,1,2] two times because the -3 in index 1 and in index 2 will add up to 0 with index 3 and 4


# Time Complexity O(n)^2
#Space: O(1) or O(n)

def threeSum( nums: list[int]) -> list[list[int]]:
    #sort list to not have all the same values next to each other
    nums.sort()
    #make a list to store triplets
    triplets = []
    #make sure it doesn't have the same value in the same
    for i, v in enumerate(nums):
        #make sure that the next value is not the same as the previous one since we need a unique value for the first index of each triplet list``
        if i>0 and v == nums[i-1]:
            continue
        #get a lp and rp to see if they add up to 0
        lp = i+1
        rp = len(nums)-1
        while lp < rp :
            total = v + nums[lp] + nums[rp]
            if total < 0:
                lp+=1
            elif total >0:
                rp-=1
            else: #if total = 0
                triplets.append([v, nums[lp], nums[rp]])
                #we need to move lp to the right once so we don't add the same triplet again
                lp+=1
                #need to check that the new value is not the same as the previous one in the nums array
                while nums[lp] == nums[lp-1] and lp<rp:
                    lp+=1
    return triplets


nums = [-3,3,4,-3,1,2]
print(threeSum(nums))

# Time complexity
# sorting array is O(n log n)
# one loop for the first i value and a second loop that has an inside loop to solve for j and k. So we have two nested loops
# the two nested loops give us O(n)^2

# O(n log n) + O(n)^2 = O(n)^2

# Space Complexity can be O(1) or O(n) depending on the library or implementation
#

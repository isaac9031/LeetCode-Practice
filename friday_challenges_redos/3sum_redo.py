def threeSum(nums: list[int]) -> list[list[int]]:
    #we have to have unique triplets, so i != j, i != k, and j != k in the triplet [nums[i], nums[j], nums[k]] = 0
    triplets = [] #needed to save the unique triplets that add up to 0
    nums.sort() #sorting in order to make it easy when it comes to the triplet_total
    #start with a for loop for the first index that we have to insert in the triplets. Needed since we have three indeces to take care of
    for i, v in enumerate(nums): #using enumerate so we can use the index and the value
            #check that the next i is not the same as the previous one
        if i > 0 and v == nums[i-1]: #we skip current iteration if the previous nums[i-1] is the same as the current one
            continue
        j = i+1 #will take care of the second index in the triplet
        k = len(nums)-1 #will take care of the third index in the triplet
        #now we have the first triplet, we need to check that it adds up to 0, if it doesn' then we need to use a while loop to go over index j and k
        while j < k:
            triplet_t = v + nums[j] + nums[k]
            if triplet_t == 0:
                triplets.append([v,nums[j],nums[k]]) #if it is a triplet then we need to move the j pointer so the loop doesn't run idefinitly
                j+=1        #need the while loop to not have the same value in the same index of a triplet two times *****
                while j<k and nums[j] == nums[j-1]:   #we cannot repeat j for the same index in a triplet since we need unique ones, so we move it until its not the same value
                    j+=1
            elif triplet_t < 0:
                j+=1
            else:
                k-=1
    return triplets

nums = [-1,0,1,2,-1,-4]  #[-4,-1,-1,0,1,2]
print(threeSum(nums))

#*******
#example of why we need the second while loop
#if we have [0,-1,-1,-1,2,4]
#we will first have [0,-1,-1] for the first  triplet
#without the while loop we will have another [0,-1,-1] since index 2 and 3 are the same value


# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63ddad31ff57d05f33aceba8

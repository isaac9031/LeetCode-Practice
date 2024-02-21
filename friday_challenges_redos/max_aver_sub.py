def findMaxAverage( nums: list[int], k: int) -> float:
    lp = 0
    rp = k #change it from k-1 to just k since total is already considering k-1
    total = sum(nums[:k]) #will give us the sum of the first four elements
    maximum = total #added this since we have to compare the maximum with the new total
    #we are going to have to move both lp and rp to the right together
    #the rp can't be greater than the len of the list
    while rp < len(nums):
        newtotal = total + nums[rp] - nums[lp]
        maximum = max(newtotal, maximum)
        lp+=1
        rp+=1
    return maximum/k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))

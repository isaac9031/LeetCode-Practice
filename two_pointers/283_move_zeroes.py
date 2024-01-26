def moveZeroes(nums: list[int]) -> None:
    #the value that is nonzero needs to be moved to the right so we can switch it, and then make the new i to be the 0 that has been moved to the right
    #if there are two zeros next to each other then we have to add each of those to the end. should i just count the # of zeros so it just adds them?
    i = 0
    j = 0
    while j < len(nums):
        if nums[i] == 0:
            if nums[j] != 0:
                nums[i],nums[j]= nums[j], nums[i]
                i+=1
        j+=1
    return nums



nums = [0, 0, 1, 3, 0, 12, 0]
print(moveZeroes(nums))

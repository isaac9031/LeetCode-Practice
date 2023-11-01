def countPairs(nums: list[int], target: int) -> int:
    j = 0
    total = 0

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if i < j:
                if nums[i] + nums[j] < target:
                    total+=1
    return total


nums = [-6,2,5,-2,-7,-1,3]  #will have to go 0,1, 0,2 ....1,1 1,2...
target = -2
print(countPairs((nums), target))

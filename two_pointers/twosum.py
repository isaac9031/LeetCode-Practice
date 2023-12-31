def twoSum(nums: list[int], target: int) -> list[int]:
    for l in range(len(nums)):
        r = len(nums)-1
        while l < r:
            current_total = nums[l] + nums[r]
            if current_total == target:
                    return [l,r]
            else: #move the left to the right if we need a greater value to get the total
                r-=1
            # else:#move the right to the left if we need a smaller value to get the total
            #     l+=1


print(twoSum([2,7,11,15], 9))

print(twoSum([-3,4,3,90], 0))

print(twoSum([3,2,4], 6))


print(twoSum([-10,-1,-18,-19], -19))

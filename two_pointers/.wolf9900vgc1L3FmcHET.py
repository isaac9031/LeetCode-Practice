def twoSum(nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums)-1
    while l < r:
        current_total = nums[l] + nums[r]
        if current_total == target:
                return [l,r]
        elif target < current_total: #move the left to the right if we need a greater value to get the total
            r-=1
        else:#move the right to the left if we need a smaller value to get the total
             l_=1


# print(twoSum([2,7,11,15], 9))

# print(twoSum([-3,4,3,90], 0))

print(twoSum([3,2,4], 6))

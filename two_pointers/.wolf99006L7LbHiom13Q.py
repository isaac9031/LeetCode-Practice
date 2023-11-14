def twoSum(nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums)-1
    while l < r:
        current_total = nums[l] + nums[r]
        if current_total == target:
                return [l,r]
        elif target > current_total:
            l+=1
            

print(twoSum([2,7,11,15], 9))

print(twoSum([-3,4,3,90], 0))

#the three is greter than 0
#if the target is less than the right then we decrease r by one and keep l the same
# once it reaches 7 it keeps that r the same since the target is greater than the nums[r] value
# now it checks if the current nums[l] + nums[r] equal target, which they do so it returns l and r


#if nums = [3,2,4], target = 6 then it will go to the else first to see if nums[l]"3"+nums[r]"4"
#..if they both total 6, since it doesn't it moves the l to the right one, then it loops again..
#goes to the else wher "2" and "4" == 6 so it returns those indeces

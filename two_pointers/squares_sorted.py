#Using pointers
def sortedSquares(nums: list[int]) -> list[int]:
    new_one = []

    left, right = 0, len(nums)-1
    while left <= right: #end the loop before they cross each other
        if nums[right] * nums[right]>nums[left]*nums[left]:
            new_one.append(nums[right]*nums[right])
            right-=1
        else:
            new_one.append(nums[left]*nums[left])
            left+=1
    return new_one[::-1]


nums = [-5,-3,-2,-1]
print(sortedSquares(nums))


#Two pointer approach BEST time space complexity O(n)
#makes a list ans = [0, 0, 0, 0] then it replaces the k with the greatest one
#it moves the left ^ if it is greater than the right, it moves the right one down if its greater than the current left
def sortedSquares(nums: list[int]) -> list[int]:

    n = len(nums)
    l, r = 0, n - 1
    k = n - 1
    ans = [0] * n
    while k >= 0:
        if abs(nums[l]) > abs(nums[r]):
            ans[k] = nums[l] * nums[l]
            l += 1
        else:
            ans[k] = nums[r] * nums[r]
            r -= 1
        k -= 1
    return ans

nums = [-5,-3,-2,-1]
print(sortedSquares(nums))

#brute force aproach
# def sortedSquares(nums: list[int]) -> list[int]:
#     new_one = []
#     for num in nums:
#         new_one.append(num*num)
#     return sorted(new_one)


# nums = [-4,-1,0,3,10]
# print(sortedSquares(nums))

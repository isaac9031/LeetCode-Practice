#Using pointers
def sortedSquares(nums: list[int]) -> list[int]:
    new_one = []
    for num in nums:
        new_one.append(num*num)
    print(new_one)

    mp = len(nums)-1 #will print 4
    left, right = 0, len(nums)-1
    while left <= right:
        if new_one[right]>new_one[left]:
            new_one[mp] = new_one[right]
            right-=1
        else:
            new_one
        mp -= 1


    return new_one


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

# Move all 0s to the right without making a copy of the array
#Time-complexity:O(N)   space Complexity:O(1)
def moveZeroesRight(nums: list[int]) -> None:
    #the value that is nonzero needs to be moved to the right so we can switch it, and then make the new i to be the 0 that has been moved to the right
    #if there are two zeros next to each other then we have to add each of those to the end. should i just count the # of zeros so it just adds them?
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] != 0:
            nums[i],nums[j]= nums[j], nums[i]
            i+=1
        j+=1
    return nums



nums = [1,0,1]

print(moveZeroesRight(nums))




# Time Complexity:
# The time complexity is determined by the number of basic operations the
# algorithm needs to perform in terms of the size of the input nums. In your case:

# While Loop: The loop runs until j reaches the length of the list (len(nums)),
# so it performs a constant number of operations for each element in the list.

# Constant-Time Operations Inside the Loop:

# Checking if nums[j] is nonzero.
# Swapping nums[i] and nums[j].
# Incrementing i and j.
# Therefore, each iteration of the loop performs a constant number of operations.
# Since you iterate through the entire list once, the overall time complexity is O(N), where N is the length of the input list.

# Space Complexity:
# The space complexity refers to the additional memory space required
# by the algorithm, excluding the input. In your function:

# Indices (i and j): These are integer variables that store indices.
# Their space requirements are constant, regardless of the size of the input.

# Other Variables: There are a few additional variables used for temporary storage,
# but their space requirements are constant.

# Since the amount of extra space used by the algorithm is constant (it does not depend on the size of the input list),
# the space complexity is O(1).

# In summary:

# Time Complexity: O(N) (linear time complexity)
# Space Complexity: O(1) (constant space complexity)



def moveZeroesLeft(nums: list[int]) -> None:
    #exchange a number whenever ther is a zero on the left
    #we need two pointers to keep track of the left and right value
    i=0
    j=0
    while j<len(nums):
        if nums[j]==0:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
        j+=1



    return nums


nums = [1,0,1]
nums1 = [0,1,0,3,12]

print(moveZeroesLeft(nums))
print(moveZeroesLeft(nums1))

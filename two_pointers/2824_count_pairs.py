# Count Pairs Whose Sum is Less than Target
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


def countPairs(nums: list[int], target: int) -> int:
    nums.sort() # sort nums   [-7, -6, -2, -1, 2, 3, 5]
    count = 0 # variable to store the count
    left = 0 # variable to store the left
    right = len(nums)-1 # variable to store the right
    while(left < right): # loop until left is less than right
        if(nums[left] + nums[right] < target):
            count += right-left # update the count
            left += 1 # increment the left pointer
        else: # else
            right -= 1 # decrement the right pointer
    return count # return the count


nums = [-6,2,5,-2,-7,-1,3]
target = -2
print(countPairs((nums), target))
#notes using two-pointers
#sorted list [-7, -6, -2, -1, 2, 3, 5]
#this problem will increase pointer left by one if the total is less than target
#will move right pointer to the left once if total is more than target

#l=0 r=6 idx
#the first loop will move the pointer on the right to the left once since -7+5 = -2, which is not less than the target
#it goes thru the else statement

#l=0 r=5 idx
#on the second loop it will count 5 pairs 5-0 , it will go thru the if statement since (-7+3)less than -2(target), some of the pairs: -7+2, -7+-1, -7+-2 etc.
#we finished counting the numbers that add to -7 and will be less thatn -2, moves left tot he right once

# l=1 r=5 idx
#third loop - now we will count how many numbers can be added to -6 and still be less than the targe -2,
#count will be increased by 4 since we will get it by '5-1=4' so it passes the if statment. any number in between -6and3 will give us a total that is less than the target '-6+3=-3','-6+2=-2'...etc. then moves the left pointer to right once
# ..we exclude -7 since we already paired with -6 before and also 5 since we know from before that it will be sum greater than the target(like -6+5 = -1, which is greater than -2)

# l=2 r=5 idx
#on the next loop it will start at -2 left and 3 right. it will not go pass the if statement since -2+3=1, so it will do the else which move the r idx to the left once

# l=2 r=4 idx
#on the fifth loop the if statement checks -2+2, it doesnt pass the if loop since 0>2
#moves r indx to the left once

## l=2 r=3 idx
#now the if checks if -2+-1<-2 so it passes and adds one the the count and moves the left to the right once

#l=3 r=3 this is where the loop ends

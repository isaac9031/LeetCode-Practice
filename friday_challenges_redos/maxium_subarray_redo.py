def maxSubArray( nums: list[int]) -> int:
    if len(nums)<1:
        return 0
    left, right = 0, 0
    max_value = float("-inf") #keeps track of the max value even if it is negative
    window_sum = 0
    while right < len(nums):
        window_sum += nums[right]
        right+=1 #this makes sure that the right moves and also that it keeps moving if the next while loop is false, which makes the window grow
        max_value = max(max_value, window_sum)
        #we now remove the values before the one that makes window_sum negative. We still keep the maximum value in the max_value variable, even if it is negative
        while left<right and window_sum<0: #makes sures that the window keeps moving right(left+=1) if the window sum is still negative, then it goes back to the first loop if positive
            window_sum -= nums[left]
            left+=1
    return max_value


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

# while left<right and window_sum<0: #makes sures that the window keeps moving right(left+=1) if the window sum is still negative. it goes back to the first loop if the window_sum becomes positive
#when it gets to -3 it will add it to 1, which will make the window_sum = -2, then it will get inside the second while loop, there..
#.. we will first remove the 1 from the left(making window_sum=-3) and move the index left now will be 2...
#..then it will go thru the same loop again since right index = 3 and left = 2.
#The -3 now will be removed from window sum and we will have 0 as the window sum, and then left index of 3,  which will make it go back to the first loop and increase right index
#now both left and right are 3, this will make sure to have a window_sum=4 and move the right index> 4.
#now our max value will be 4 since max_value = max(1, 4), it will loop once more in the same while looop since our window sum is positive
#now it will add window_sum = 4 +-1, which will still give us a positive window sum of 3, so it will still stay in the same value loop and keep the max value as 4
#we now add 2 and the new window sum is 5, which will be our new max value
#then in the next loop on the same while loop it will add 1, and the new window sum is 6, which will be our new max value
#then it will still stay in the same loop and add -5 making the window sum 1, and still max value as 6
#in the last loop it will add 4, which will give us a window sum of 5, which is less than the current max value of 6






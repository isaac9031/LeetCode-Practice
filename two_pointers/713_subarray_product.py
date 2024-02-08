# Given an array of integers nums and an integer k, return the number of contiguous
# subarrays where the product of all the elements in the subarray is strictly less than k.

def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    #multiply current times the next one, we need an empty list to multiply those values
    #since contigues we can use two pointers next to each other
    if len(nums)<=1:
        return 0
    ans = 0  #will count each subarray that is less than k
    lp = 0 #will be used to keep track of the left sid of the array
    sub_total = 1 #keeps track of the total of that subarray
    for rp in range(len(nums)):
        sub_total *= nums[rp]
        while sub_total >= k and lp<=rp: #if subtotal greaten than k then ...
            sub_total/=nums[lp] #..remove the previous element by which subtotal was multiplied. Multiplictation cancels division and vice versa
            lp+=1 #move the lp to the right, so both lp and rp do not consider that value.
        if sub_total<k:
                print("Subarray:", nums[lp:rp+1], "Subtotal:", sub_total)
                #rp-lp makes sure to add one subarray if there is more than one element in it. takes care of the subarrays with only one element and the one with multiple element. ex. [5,2] will add two to ans since index 2-1 = 1 + 1(for the new individual element)
                ans+=rp - lp + 1 #When the condition sub_total < k is satisfied, it means that the current subarray from lp to rp (inclusive) has a product less than k
    return ans

nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))

#  The + 1 in rp - lp + 1 accounts for the individual element itself, ensuring that it is counted as a valid subarray if its product is less than k.
# Consider the case where rp and lp point to the same element. In this case, rp - lp + 1 evaluates to 0 - 0 + 1 = 1, ensuring that the single element subarray is counted as valid.
# So, the + 1 ensures that both single-element subarrays and multi-element subarrays are correctly counted as valid subarrays if their product is less than k.

# When rp and lp point to the same element, rp - lp + 1 equals 1, correctly accounting for the single-element subarray.
# When rp moves forward and lp remains the same, rp - lp + 1 equals the length of the subarray, correctly accounting for subarrays with multiple elements.
# As rp continues to move forward, lp may also move forward, ensuring that the expression rp - lp + 1 continues to accurately reflect the length of the current subarray being processed.
# This approach effectively handles both single-element and multi-element subarrays, ensuring that each valid subarray is counted exactly once in the final result.







##time excceeding.  lOOK at video and the booked mark
# def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
#     #make a list to add all the subarrays that add up to less than k
#     #multiply current times the next one, we need an empty list to multiply those values
#     #since contigues we can use two pointers next to each other
#     sub_arrays = 0
#     lp = 0
#     rp = 1

#     if k < 0 :
#         return 0

#     else:
#         while lp < len(nums):
#             if nums[lp] < k:
#                 sub_arrays +=1
#                 total = nums[lp]
#                 while rp < len(nums) and total*nums[rp] < k:
#                     total*=nums[rp]
#                     sub_arrays+=1
#                     rp+=1

#                 lp+=1
#                 rp=1+lp
#             else:
#                 return 0


#         return sub_arrays



# nums = [1,1,1]
# k = 1
# print(numSubarrayProductLessThanK(nums, k))

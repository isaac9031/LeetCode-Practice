# Given an array of integers nums and an integer k, return the number of contiguous
# subarrays where the product of all the elements in the subarray is strictly less than k.


def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    #make a list to add all the subarrays that add up to less than k
    #multiply current times the next one, we need an empty list to multiply those values
    #since contigues we can use two pointers next to each other
    sub_arrays = 0
    lp = 0
    rp = 1

    if k < 0 :
        return 0

    else:
        while lp < len(nums):
            if nums[lp] < k:
                sub_arrays +=1
                total = nums[lp]
                while rp < len(nums) and total*nums[rp] < k:
                    total*=nums[rp]
                    sub_arrays+=1
                    rp+=1
                lp+=1
                rp=1+lp
                


        return sub_arrays



nums = [1,1,1]
k = 1
print(numSubarrayProductLessThanK(nums, k))

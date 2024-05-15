# Given an array arr, replace every element in that array with the
# greatest element among the elements to its right, and replace the
# last element with -1.

# After doing so, return the array.
#using pointers
class Solution(object):
    def replaceElements(self, arr):
        new_list = []
        lp = 0
        for i in range(len(arr)-1):
            lp = i+1
            rp = lp+1
            maximum = arr[lp]
            while rp<len(arr)-1:
                if arr[rp]>arr[lp]:
                    maximum = arr[rp]
                    lp = rp
                    rp+=1
                rp+=1
            new_list.append(maximum)
        new_list.append(-1)
        return new_list

arr = [17,18,5,4,6,1]
print(Solution().replaceElements(arr))

#set the maximum to be the second value at the begining
#check from 1 to 5 and find the maximum, start with lp and rp next to it compare it
# make maximum = arr[lp], then compare arr[rp]>arr[lp], now the new maximum is arr[rp]
#now lp=rp and rp+=1.
#if maximum is still lp then we only move rp.
# then move the lp to the right one as well as the rp

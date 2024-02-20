# You are given an integer array height of length n. There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

#Brute Force -> Then we use two pointer solution
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # res = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = (j-i)*min(height[i],height[j])
        #         res = max(res, area)
        # return res
        res = 0
        lp = 0
        rp = len(height)-1
        while lp<rp:
            area = (rp-lp)*min(height[lp],height[rp])
            res = max(area, res)
            if height[lp]<height[rp]:
                lp+=1
            elif height[lp]>height[rp]:
                rp-=1
            else:
                rp-=1
        return res

container1 = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(container1.maxArea(height))

# Notes
# Unlike the nested loop approach in your first solution, which..
# ..iterates over all possible pairs, the two-pointer approach only requires a single pass ..
# ..through the array. This significantly reduces the number of iterations and improves the algorithm's efficiency.


# Brute-force approach: O(n^2)
# Two-pointer approach: O(n)

# In Big O notation:

# O(n^2) means the algorithm's time complexity grows quadratically with the size of the..
# ..input (i.e., for every increase in the input size by 1, the time it takes to run the algorithm increases by the square of 1).

# O(n) means the algorithm's time complexity grows linearly with
# the size of the input (i.e., for every increase in the input size by 1, the time it takes to run the algorithm increases by only 1).

# You are given an integer array height of length n. There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.


class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        lp = 0
        rp = len(height)-1
        while lp < rp:
            area = (rp-lp)*min(height[lp],height[rp])
            res = max(area, res)

            if height[lp] < height [rp]:
                lp+=1
            elif height[lp] > height [rp]:
                rp-=1
        return res


container1 = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(container1.maxArea(height))

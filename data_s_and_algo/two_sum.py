class Solution():
    def twoSum(self, nums: list[list], target:int)-> list:
        keep_track = {}
        for i, e in enumerate(nums):
            dif = target - e
            if dif in keep_track:
                    return [i, keep_track[dif]]
            keep_track[e] = i

nums = [2,7,11,15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)

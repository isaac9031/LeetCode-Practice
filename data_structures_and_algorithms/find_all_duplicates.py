class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        d = {}
        lista = []
        for n in nums:
            d[n] = d.get(n,0)+1

        for key, value in d.items():
            if value == 2:
                lista.append(key)
        return lista

solution = Solution()
nums = [4,3,2,7,8,2,3,1]
result = solution.findDuplicates(nums)
print(result)

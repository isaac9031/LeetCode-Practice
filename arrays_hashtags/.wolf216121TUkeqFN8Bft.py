class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0,0
        print(len(s),len(t))
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                                    #     j+=1
                                    # else:
                                    #     j+=1
        if i == len(s):
            return True
        return False



solution = Solution()
s = "ab"
t = "baab"
nums = [1,2,2]
result = solution.isSubsequence(s,t)
print(result)

class Solution():
    def isPalindrome(self, x:int) -> bool:
        x = str(x)
        print(x[::-1])

        for l in x:
            reversed = x[::-1]
            print(reversed)
            if x == reversed:
                return True
            return False

solution = Solution()
x =-121
result = solution.isPalindrome(x)
print(result)

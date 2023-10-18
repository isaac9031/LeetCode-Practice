class Solution():
    def fib(self, n:int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

solution = Solution()
n = 5
result = solution.fib(n)
print(result)

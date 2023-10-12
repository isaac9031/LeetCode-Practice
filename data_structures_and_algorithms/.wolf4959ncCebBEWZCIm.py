class Solution(object):
    def countPrimes(self, n):

        lista = []
        j=1
        while j < n:
            for i in range(1,n):
                if i % j != 0:
                    j+=1
                lista.append(i)

solution = Solution()
n = 10
result = solution.countPrimes(n)
print(result)


#it cannot be divided by anything else execpt itself
#

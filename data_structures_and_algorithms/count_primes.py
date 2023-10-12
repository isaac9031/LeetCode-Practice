# class Solution(object):
#     def countPrimes(self, n):
#         total = 0 #used to save  numbers that are prime
#         for i in range(2, n): #geneate sequence from 0 to n
#             if is_prime(i):
#                 total += 1
#             print(i, total)
#         return total

# def is_prime(number): #divide the number by everything, except number itself
#     if number == 0 or number == 1:
#         return False
#     if number == 2:
#         return True
#     else:
#         for j in range(2, number):
#             print(number, j)
#             if number % j == 0:
#                 return False
#         return True


# solution = Solution()
# n = 10
# result = solution.countPrimes(n)
# print(result)


#Prime number is a number that can be divided by 1 and by itself to get 0, ex n =10
#there are 4 prime numbers less than 10, these are 2,3,5,7


class Solution(object):
    def countPrimes(self, n):
        total = 0
        if n <= 2:
            return 0
        for i in range(2, n):
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                total += 1
        return total

solution = Solution()
n = 10
result = solution.countPrimes(n)
print(result)


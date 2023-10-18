#Using Concatation helps to only need two coditions
class Solution(object):
    def fizzBuzz(self, n):
        lista  = []
        for i in range(1,n+1):
            new_string = ""
            if i % 3 == 0:
                new_string = "Fizz"
            if i % 5 == 0:
                new_string += "Buzz"
            if not new_string:
                new_string+= str(i)
            lista.append(new_string) 
        return lista


solution = Solution()
n = 3
result = solution.fizzBuzz(3)
print(result)


#We had to check three conditions
# class Solution(object):
#     def fizzBuzz(self, n):
#         lista  = []
#         print(range(n))

#         for i in range(1,n+1):
#             if i % 3 == 0 and i % 5 ==0:
#                 lista.append( "FizzBuzz")
#             elif i % 3 == 0:
#                 lista.append("Fizz")
#             elif i % 5 == 0:
#                 lista.append("Buzz")
#             else:
#                 lista.append(str(i))
#         return lista

# solution = Solution()
# n = 3
# result = solution.fizzBuzz(3)
# print(result)

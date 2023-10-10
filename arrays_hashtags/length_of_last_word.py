
class Solution(object):
    def lengthOfLastWord(self, s):
        lista = s.strip().split(" ")

        return len(lista[-1])

solution = Solution()
s = "   fly me   to   the moon  "
result = solution.lengthOfLastWord(s)
print(result)


# This solution gets rid of the white spaces in between words:
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         lista = s.strip().split(" ")
#         print(lista)
#         new = []
#         for word in lista:
#             if word != "":
#                 new.append(word)
#         print(new)
#         return len(new[-1])



# solution = Solution()
# s = "   fly me   to   the moon  "
# result = solution.lengthOfLastWord(s)
# print(result)

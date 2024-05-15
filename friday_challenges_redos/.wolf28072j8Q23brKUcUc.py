# class Solution(object):
#     def isSubsequence(self, s, t):
#         #separate string into a list to go over each char, then add to a list then compare both lists
#         listaT = []
#         for n in t:
#             if n in s:
#                 listaT.append(n)
#         print(listaT)
#         listaT = "".join(listaT)
#         if s == listaT:
#             return True
#         else:
#             return False



# solution =  Solution()
# s = "abc"
# t = "ahbgdc"
# print(solution.isSubsequence(s,t))


def isSubsequence( s, t):
    i, j = 0, 0
    while i<len(s) and j<len(t):
        if s[i] == t[j]:
            i+=1



    pass

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))

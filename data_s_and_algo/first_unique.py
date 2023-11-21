# class Solution(object):
#     def firstUniqChar(self, s):
#         dic_char = {}
#         for l in range(len(s)):
#             if s[l] not in dic_char:
#                 dic_char[s[l]] = 0   # a : 2   b:2
#             dic_char[s[l]]+=1
#         print(dic_char)
#         for key, value in dic_char.items():
#             if value == 1:
#                 return s.find(key)
#         return -1

# solution = Solution()

# s = "leetcode"
# result = solution.firstUniqChar(s)
# print(result)

#time complexity o(n) , space o(n)
#better solution ⬇️ uSES HASHMAP
#uses d.get(char, 0) instead of using # if d[char] not in d:
#this gets the value> d.get(key, default)    d[char] = 0
#                                        d[char] += 1
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         d = {}
#         for char in s:
#             d[char] = d.get(char,0) + 1 #adds the key : d.get grabs the value if the key already exists
#                                         #..if it doesn't then it default to 0, then it adds the +1
#         for i , char in enumerate(s):
#             if d[char] == 1:
#                 return i
#         return -1
# solution = Solution()

# s = "loveleetcode"
# result = solution.firstUniqChar(s)
# print(result)

#using string
class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in range(len(s)):
            #checks in the front
            print(s[i+1::])
            #checks behind
            print(s[:i])
            if s[i] not in s[i+1::] and s[i] not in s[:i:]:
                return i
        return -1

solution = Solution()
s = "loveleetcode"
result = solution.firstUniqChar(s)
print(result)

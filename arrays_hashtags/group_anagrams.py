# Study Solutions
# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         res = {}
#         for s in strs:
#             count = [0] * 26 # a .... z
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             key = tuple(count)
#             if key in res:
#                 res[key].append(s)
#             else:
#                 res[key] = [s]

#         return list(res.values())

# solution = Solution()
# strs = ["eat","tea","tan","ate","nat","bat"]
# result = solution.groupAnagrams(strs)
# print(result)

        #need to find the ones that are the same to each other
        #put them in the a list
        #need a for loop to access each word and count the amount of each letter on every string
        #if they have the same amount of of each type of letten then add it to the list
        #will need a dictinary to keep track


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_table = {}

        for string in strs:
            print(sorted(string))
            print(''.join(sorted(string)))
            sorted_string = ''.join(sorted(string))
            if sorted_string not in strs_table:
                strs_table[sorted_string] = []

            strs_table[sorted_string].append(string)
        print(strs_table)

        return list(strs_table.values())
solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = solution.groupAnagrams(strs)
print(result)
# Time complexity: O(m*nlogn))
# Space complexity: O(n)

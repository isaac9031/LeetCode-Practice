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


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    #sort all strings inside the list
    #need a dictionary to save them
    diccionario = {}
    for string in strs:
        sort_list = sorted(string)  #will make a list for each. ex : ['a','e', 't']. sorted_list is a list
        sort_string = ''.join(sort_list) #''.join(sorted_string) takes all elements in a list and joins them into a string, no string separator''
                                                #/...Ex:  aet  now sorted_string is a string
        if sort_string not in diccionario:
            diccionario[sort_string] = []  #used [] because we want a list as the value, which we add strings next.  didn't use diccionario[sort_string]=string since we want a list of all the words that are the same, not only one string, but a list of strings
        diccionario[sort_string].append(string) #adding to the [], which is in the value side, if it already exists
    print(diccionario.values())
    return list(diccionario.values())  #list() can only create a list from an iterable object such as dictionaries, strings, tuples. The list() function occupies more space than the [] method



strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))


# list. sort() will sort the list in-place, mutating its indexes and returning None ,
# whereas sorted() will return a new sorted list leaving the original list unchanged.
#  Another difference is that sorted() ACCEPTS ANY ITERABLE while list.sort() is a
# method of the list class and can ONLY BE USED WITH LISTS
# Time complexity: O(m*nlogn))
# Space complexity: O(n)

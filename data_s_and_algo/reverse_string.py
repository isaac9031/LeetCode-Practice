# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
#does not use return

class Solution(object):
    def reverseString(self, s):
        s[:] = s[len(s)-1::-1] #modifies input in place
        # print(s)
        return s

solution = Solution()
s = ["h","e","l","l","o"]
result = solution.reverseString(s)
print(result)


#this is using way more memory      ^^top one uses  O(1) memory
#  In slicing, the stop index is
# ..not included in the result, but in range(), the stop value is included.

# class Solution(object):
#     def reverseString(self, s):
#           reversed_list = []
            # print(len(s))
            # for l in range(len(s)-1,-1, -1): #start(will start at index 4) stop(index 0, we use -1 so it stops at 0) step(-1)
            #     reversed_list.append(s[l])
            # return reversed_list
# solution = Solution()
# s = ["h","e","l","l","o"]
# result = solution.reverseString(s)
# print(result)

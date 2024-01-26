
# Given two strings s and t, return true if they are equal when both
# are typed into empty text editors. '#' means a backspace character.
# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_characters(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack
        #the function remove_characters(s)or(t) needs to be called in order to "activate"
        #it is called in the return remove_characters(s), it will pass the s argument to the function remove_characters first for s, then for
        return remove_characters(s) == remove_characters(t) #['a', 'c'] =['a', 'c']

s = "ab#c"
t = "ad#c"
solution = Solution()
print(solution.backspaceCompare(s,t))
#delete the char behind # if is not a #,
#if more than one #, then delete the same amount of char



def backspaceCompare(s, t):

    #use of helper function
    def nextValidChar(str, index):
        backspace = 0 #will be used to skip its own index with index-=1 and then again when it goes to the elif because of "b"
        while index >=0: #it loops two times if it finds a #, first one is to skip the #, second one is to skip the char to the left of it. both use index-=1
            if backspace ==0 and str[index] != '#':
                break #used to not change the index if str[index] is not # and if there is no backspaces. it breaks and returns index
            elif str[index] == '#': #will add a backspace for every # found
                backspace +=1
            else:
                backspace-=1 #will remove a backspace if str[index] != #, since it was a nonpound character
            index -=1  #when its a "#", on the first loop it will skip the # . on the second it will skip the first char on the left of #
        return index

    index_s = len(s) - 1
    index_t = len(t) - 1
    while index_s >=0 or index_t >=0 :
        index_s = nextValidChar(s, index_s)
        index_t = nextValidChar(t, index_t)

        char_s = s[index_s] if index_s >= 0 else ""
        char_t = t[index_t] if index_t >= 0 else ""
        if char_s != char_t:
            return False
        index_s -= 1
        index_t -=1
    return True



s = "ab##c"
t = "adc#c"
print(backspaceCompare(s,t))




def backspaceCompare(s, t):
    #function to check each character and skip the same amount of # and chr to the left
    def validChar(str, index):
        backspace = 0
        while index >=0:
            if str[index] != "#" and backspace == 0:
                break
            elif str[index] == "#":
                backspace +=1
            else:
                backspace-=1
            index-=1
        return index
    #while loop to check each element that is not a #
    index_s = len(s)-1
    index_t = len(s) -1
    while index_s >= 0 or index_t>=0:
        index_s =  validChar(s, index_s)
        index_t = validChar(t, index_t)

        char_s = s[index_s] if index_s >=0 else  ""
        char_t = s[index_t] if index_t >=0 else ""

        if char_s != char_t:
            return False

        index_s-=1
        index_t-=1

    return True


s = "ab#c"
t = "ac#c"
print(backspaceCompare(s,t))

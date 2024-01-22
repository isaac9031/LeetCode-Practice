
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

        return remove_characters(s) == remove_characters(t)

s = "ab#c"
t = "ad#c"
solution = Solution()
print(solution.backspaceCompare(s,t))
#delete the char behind # if is not a #,
#if more than one #, then delete the same amount of char



def backspaceCompare(s: str, t: str) -> bool:
    i, j = len(s)-1, len(t)-1
    s_skip, t_skip = 0, 0

    while i >= 0 or j >= 0:
        while i >= 0:
            if s[i] == '#':
                s_skip += 1
                i -= 1
            elif s_skip > 0:
                s_skip -= 1
                i -= 1
            else:
                break

        while j >= 0:
            if t[j] == '#':
                t_skip += 1
                j -= 1
            elif t_skip > 0:
                t_skip -= 1
                j -= 1
            else:
                break

        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False

        if (i >= 0) != (j >= 0):
            return False

        i -= 1
        j -= 1
    return True
s = "ab#c"
t = "ad#c"
print(backspaceCompare(s,t))

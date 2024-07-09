class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.strip().split(" ")[-1] #removes blank spaces, then adds each word to the list, and at the end it only selects the last word
        length = len(word) #gets length of last word
        return length



s = "luffy is still joyboy"
solution = Solution()
print(solution.lengthOfLastWord(s))

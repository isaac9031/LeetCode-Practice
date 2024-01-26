class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #we need to eliminate from right to left since we cannot compare from left to right because some char migh not be considered(skipped)
        #we need to keep track of how many times we have to backspace, will immediately backspace if we see a # and will also have to keep track of how many # there is next to each other
        #start from right to left, len-1 , check to see if the first char on the far right are the same
        index_s= len(s)-1    #both of these are used with the while loop on line 22
        index_t = len(t)-1

        def validChar(string, index): #takes care of # and char that need to be skipped
            backspace =0
            while index >=0 :
                if string[index] == "#": #adds a backspace so in the next loop it skips that
                    backspace+=1
                    index-=1
                elif backspace>0 and string[index] != "#":
                    backspace-=1
                    index-=1
                else:
                    break
            return index

        while index_s>=0 or index_t>=0:
            index_s = validChar(s,index_s)
            index_t = validChar(t,index_t)

            if index_s >= 0:
                 char_s = s[index_s]
            else:
                char_s = ""
            char_t = t[index_t]if index_t >=0 else ""


            if char_s !=  char_t:
                return False

            index_s-=1
            index_t-=1

        return True


solution = Solution()
s = "a#c"
t = "b"
print(solution.backspaceCompare(s,t))

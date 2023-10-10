class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0,0
        print(len(s),len(t))
        while i < len(s) and j < len(t):
            if s[i] == t[j]:        #in the first loop it compares "a" from s to "b" from t, since it is not the same then ..
                i+=1                # i stays at 0 index,element "a" and  index j moves to 1(line 8 of the code). ...
            j+=1                        #..Now it will compare s[0] to t[1]..since "a" == "a" the i will increase by one...
                                        #now the if will compare s[1] to t[2], "b" =! "a" so it will only add 1 to j..
        if i == len(s):                 # if will compare s[1] to t[3], "b" == "b", now it will exit the loop...
            return True
        return False

solution = Solution()
s = "ab"
t = "baab"
nums = [1,2,2]
result = solution.isSubsequence(s,t)
print(result)


# note: we can use j+=1 /n else: /n   j+=1 insted of just using j+=1 starting above line 8.

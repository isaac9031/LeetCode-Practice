class Solution(object):
    def isAnagram(self, s, t):
        num_s = {}
        num_t = {}
        if len(s) == len(t):
            for i in range(len(s)-1):
                if s[i] not in num_s:
                    num_s[s[i]] = 0
                num_s[s[i]]+=1
                if t[i] not in num_t:
                    num_t[t[i]] = 0
                num_t[t[i]]+=1
            if num_s == num_t:
                return True
            else:
                return False
        return False

solution = Solution()

s = "aacc"
t = "caac"

result = solution.isAnagram(s,t)
print(result)

#need to compare that we have the same amount of each letter in order to be anagram
#count the As then the Cs then compare it to the ones on the


#More Efficient
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count_S, count_T = {}, {}
        for i in range(len(s)):
        #creating,count_S[s[i]]key = value (1 + count_S.get(s[i],0))pairs
            count_S[s[i]]=1 + count_S.get(s[i],0) #it will check to see if there is a value inside count_S[s[i]], if its not then will start at 0 since .get is to get a value
            count_T[t[i]]=1 + count_T.get(t[i],0) # it will add 1 to the value of whatever key,t[i], we are on
        print(count_T)              # the 0 above allows to start a new key with a 0 value that later adds a 1 to it
        for c in count_T:
            if count_T[c] != count_S.get(c, 0): #it looks for the specific value of that key
                return False
        return True

solution = Solution()

s = "a"
t = "b"

result = solution.isAnagram(s,t)
print(result)
#could have used sorted as well, but it can occupy a lot of space if the string is too long

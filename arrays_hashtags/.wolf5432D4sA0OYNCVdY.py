class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = []
        counting = {}
        for n in range(len(strs)-1):
            print(strs[n]==strs[n+1])
            print(sorted(strs[n]))
            for l in strs[n]:
                counting[strs[n]]= 1 + counting.get(strs[n], 0) #add one if the key already exists in the dictionary
            print                                        #...or start one at 0 and add 1



solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = solution.groupAnagrams(strs)


        #need to find the ones that are the same to each other
        #put them in the a list
        #need a for loop to access each word and count the number of letter on each
        #if they have the same amount of of each type of letten then add it to the list
        #will need a dictinary to keep track

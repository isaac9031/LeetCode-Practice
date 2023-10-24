class Solution:
    def isPalindrome(self, s: str) -> bool:  #.join and .split()
        s = s.replace(" ",'').lower() #replaces all blank spaces with no space
        old_s = ""
        print(s)
        for l in s:
            if l.isalnum():
                old_s+=l
        print(old_s)
        if old_s == old_s[::-1]:
            return True
        return False


solution = Solution()
s = "A man, a plan, a canal: Panama"
result = solution.isPalindrome(s)
print(result)

#s.isalnum() checks to see that the element is alpha or numeric
#..with this we can eliminate any element that is not alpha or numberic such as : or ,

#note: there is also .isalpha() or .isnumeric() to check for letters and numbers

#.strip lol
# .strip(" ") eliminates white spaces at the end and beginning
                    #note . we cannot do s.strip(',') because it is...
                    #looking to remove a coma at the beginning and at the end

#s = s.replace(',', '')
# Example
# >>> s = 'Foo, bar'
# >>> s.replace(',',' ')
# 'Foo  bar'
# >>> s.replace(',','')
# 'Foo bar'
# >>> s.stri



#example of .split is used to convert from string to list
# string_1 = 'ab/cd/ef'
# split = string_1.split('/')
# # Returns ['ab', 'cd', 'ef']

# example of .join is used to convert list to string
# .join
# list_1 = ['a', 'b', 'c']
# string_1 = ', '.join(list_1)
# Returns 'a, b, c'

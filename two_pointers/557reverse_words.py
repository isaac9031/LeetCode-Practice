#USING POINTERS

# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

def reverseWords( s: str) -> str:
    s = list(s)
    #have two pointers one for the left and one for the right to switch them up
    #make the right pointer r-1 after it hits the white space, save it in a temporary one to not affect the main one
    #finish it before getting to the end so it doens't go out of bounds
    L = 0
    for R in range(len(s)):
        if s[R] == " " or R == len(s)-1:
            TempR = R-1
            if R == len(s)-1:
                TempR = R
            while L < TempR: #L is 0 and R is 4
                s[TempR], s[L] = s[L], s[TempR] #they get switched, need to move now to the next one
                L+=1
                TempR-=1
            L = R+1     #L will have to change at the end to be R+1
    return "".join(s)


s = "contest"
print(reverseWords(s))

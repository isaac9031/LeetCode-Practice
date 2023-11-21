#Using brute force
# def reverseWords( s: str) -> str:
#     new = s.split(" ")
#     print(new)
#     newlista = []
#     for string in new:
#         print(string[::-1])
#         newlista.append(string[::-1])

#     return (" ").join(newlista)

# s = "Let's take LeetCode contest"
# print(reverseWords(s))

# NOTES USING BRUTE FORCE:
#convert from string to list using .split(" ")
#use [::-1] to inverse a list at a time
#put them back together with the variable.join(" ") funciton


#USING POINTERS
def reverseWords( s: str) -> str:
    s = list(s)
    L = 0
    for r in range(len(s)):
        if s[r] == " " or r == len(s)-1:
            temp_l, temp_r = L, r-1

            if r == len(s) -1:
                temp_r = r
            while temp_l < temp_r:
                s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                temp_r-=1
                temp_l+=1
            L = r +1

    return "".join(s)



s = "Let's take LeetCode contest"
print(reverseWords(s))

#find and register when we encounter " " save it into a variable
#how can we count all the letters that we have before encountering the empty space
#how to know which will be the new left each time


#    *               4   input- n = 4
#   ***              3   input - n = 3
#  *****             2
# *******            1
#*********           0

#the triangle is made by odd numbers 1, 3, 5, 7, 9
#reduce left spaces by input*


def triangle(input):                #time complexity O(n^2) since it has print
    increment = 0
    for n in range(input+1):
        if n>=1:
            print(" "*(input-n) + "*"*(n+increment))
            increment += 1

input = 5
triangle(input)



# 1   n=1   n+0
# 3   n=2   n+1
# 5   n=3   n+2
# 7   n=4   n+3
# 9


# Time complexity O(n^2)
# One 'n' comes from the for loop, where the loop iterates 'n' times, ranging from 0 to input.
# The other 'n' comes from the print statement within the loop, where the print operation involves...
# ...creating a string of length 'n' in terms of the asterisks ('*') to be printed

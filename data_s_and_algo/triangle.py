
#    *               4   input- n = 4
#   ***              3   input - n = 3
#  *****             2
# *******            1
#*********           0

#the triangle is made by odd numbers 1, 3, 5, 7, 9
#reduce left spaces by input*


def triangle(input):
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

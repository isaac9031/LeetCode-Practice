# Complete the count_letters_and_digits function which
# accepts a parameter s that contains a string and returns
# two values, the number of letters in the string and the
# number of digits in the string
#
# Examples:
#   * "" returns 0, 0
#   * "a" returns 1, 0
#   * "1" returns 0, 1
#   * "1a" returns 1, 1
#
# To test if a character c is a digit, you can use the
# c.isdigit() method to return True of False
#
# To test if a character c is a letter, you can use the
# c.isalpha() method to return True of False
#
# Remember that functions can return more than one value
# in Python. You just use a comma with the return, like
# this:
#      return value1, value2


def count_letters_and_digits(s):
    letters = 0
    digits = 0
    for l in s:
        if l.isdigit():
            digits+=1
        if l.isalpha():
            letters+=1
    return digits , letters

print(count_letters_and_digits("casaa555555"))


def count_letters_and_digits(s):
    letters = 0
    digits = 0
    print(len(s))
    for e in s:
        if e.isdigit():
            digits +=1
        elif e.isalpha():
            letters +=1
    return letters, digits

print(count_letters_and_digits("casaa555555"))

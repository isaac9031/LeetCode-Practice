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
        letters = []
        digits = []
        for i in s:
                if i.isdigit() == True:
                        digits.append(i)
                        total_digits = len(digits)
                if i.isalpha():
                        letters.append(i)
                        total_letters= len(letters)
        return total_digits, total_letters

print(count_letters_and_digits("casaa555555"))



#Solution online
# def count_letters_and_digits(s):
#     num_letters = 0                                     # solution
#     num_digits = 0                                      # solution
#     for c in s:                                         # solution
#         if c.isdigit():                                 # solution
#             num_digits += 1                             # solution
#         if c.isalpha():                                 # solution
#             num_letters += 1                            # solution
#     return num_letters, num_digits                      # solution
#                                                      # problem

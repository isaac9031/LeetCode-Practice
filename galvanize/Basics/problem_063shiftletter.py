# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

def shift_letters(string):
    replaced = []
    for i in string:
        value = ord(i)
        if value >=65 and value <90:
            replaced.append(chr(value+1))
        elif value == 90:
            replaced.append(value-25)
        elif value >=97 and value <122:
            replaced.append(chr(value+1))
        elif value == 122:
            replaced.append(chr(value-25))
    return "".join(replaced)


print(shift_letters("striSg"))

# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# slicing works in lists, strings, and tuples.

def is_palindrome(word):
    word_str = str(word)
    if word_str[::-1] == word_str:
        return True
    else:
        return False


print(is_palindrome(44445 ))

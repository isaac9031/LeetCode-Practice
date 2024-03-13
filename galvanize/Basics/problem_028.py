# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.

def remove_duplicate_letters(s):
    new_list = []
    for letter in s:
        if letter not in new_list:
            new_list.append(letter)
    return "".join(new_list)        # will turn  ["a","p","l","e"] into aple


print(remove_duplicate_letters("appleapple"))



# def last_item(values):
#     if len(values)==0:
#         return None
#     else:
#         last_item = values[-1]
#         return last_item

# print(last_item(["a", "b"]))

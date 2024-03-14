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
    return "".join(new_list)        # will change  ["a","p","l","e"] into aple
print(remove_duplicate_letters("appleapple"))


#Removing duplicate numbers
def remove_duplicate_number(list1):
    newlist = []
    for n in list1:
        if n not in newlist:
            newlist.append(n)
    return newlist

list1 = [1, 1, 3, 4, 5, 1, 2, 3]
print(remove_duplicate_number(list1))



#Removing duplicate numbers in place
def remove_duplicates_in_place(nums):
    seen = {}
    i = 0
    while i < len(nums):
        if nums[i] not in seen:
            seen[nums[i]] = True
            i += 1
        else:
            del nums[i] #removes that specific element
            # we cannot use nums.remove(nums[i]) since it  removes  the first elements in the list that has that value, that's why the 1 at the beginning is removed

list1 = [1, 1, 3, 4, 5, 1, 2, 3]
remove_duplicates_in_place(list1)
print(list1)  # Output: [1, 3, 4, 5, 2]






# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the
# number of unique elements in nums.
class Solution:
  def removeD(self, arr):
    l = 1
    for r in range(1,len(arr)):
      if arr[r] != arr[r-1]:
        arr[l] = arr[r]
        l+=1
    return arr

sol = Solution()
print(sol.removeD([2, 3, 3, 3, 6, 9, 9]))
#4 unique numbers







#cannot use set if we are trying to have the same order after removing an element for the rest of the list
def remove_duplicate_letter(string):
    unique_letter = set(string)
    return  ''.join(unique_letter)
string = 'Hello World Hello'
print(remove_duplicate_letter(string))



def remove_duplicate_words(a_string):
    a_string = a_string.split()
    unique_words = set(a_string)
    return ''.join(unique_words)
a_string = 'Hello World Hello'
print(remove_duplicate_words(a_string))

def remove_duplicate_n(numbers):
    unique_numbers = set(numbers)
    return unique_numbers

numbers = [1, 1, 3, 4, 5, 1, 2, 3]
print(remove_duplicate_n(numbers))





def last_item(values):
    if len(values)==0:
        return None
    else:
        last_item = values[-1]
        return last_item

print(last_item(["a", "b"]))

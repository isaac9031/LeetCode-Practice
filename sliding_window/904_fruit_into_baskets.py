# You are visiting a farm that has a single row of fruit trees arranged from left to right.
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit.
# There is no limit on the amount of fruit each basket can hold. Starting from any tree of your choice, you must pick
# exactly one fruit from every tree (including the start tree) while moving to the right.
# The picked fruits must fit in one of your baskets. Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

#default_factory: A function returning the default value for the dictionary
# defined. If this argument is absent then the dictionary raises a KeyError
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        tr = {}  # Dictionary to track the count of each fruit type
        l = r = 0  # Pointers to track the left and right boundaries of the sliding window
        res = 0  # Variable to store the maximum number of fruits that can be collected

        # Iterate until the right pointer reaches the end of the list
        while r < len(fruits):
            # Update the count of the current fruit in the dictionary
            if fruits[r] not in tr:
                tr[fruits[r]] = 1
            else:
                tr[fruits[r]] += 1

            # Adjust the sliding window if more than 2 fruit types are encountered
            while len(tr) > 2:
                tr[fruits[l]] -= 1  # Decrement the count of the fruit at the left boundary
                if tr[fruits[l]] == 0:
                    del tr[fruits[l]]  # If count becomes zero, remove the fruit type from the dictionary
                l += 1  # Move the left boundary of the window to the right

            # Update the result by taking the maximum of current result and the window size
            res = max(res, r-l+1)  # Adding 1 because 'l' is non-inclusive
            r += 1  # Move the right boundary of the window to the right

        return res  # Return the maximum number of fruits that can be collected

baskets = Solution()  # Create an instance of the Solution class
fruits = [3,3,3,1,2,1,1,2,3,3,4]  # Example list of fruits
print(baskets.totalFruit(fruits))  # Print the maximum number of fruits that can be collected



# Brute Force
# class Solution:
#     def totalFruit(self, fruits: list[int]) -> int:
#         max_trees = 0  # Initialize the maximum number of trees that can be collected

#         # Loop through each fruit in the list
#         for i in range(len(fruits)):
#             num_fruits = {}  # Dictionary to store the count of each fruit type
#             fruit_types = 0  # Counter for the number of different fruit types encountered

#             # Iterate through the fruits starting from index 'i'
#             for j in range(i, len(fruits)):
#                 # If the fruit type is not encountered yet, add it to the dictionary
#                 if fruits[j] not in num_fruits:
#                     fruit_types += 1  # Increment the count of different fruit types
#                     if fruit_types > 2:  # If there are more than 2 types of fruits encountered, break the loop(gets out of the for loop)
#                         break
#                     num_fruits[fruits[j]] = 1  # Add the fruit type to the dictionary with count 1
#                 else:
#                     num_fruits[fruits[j]] += 1  # If fruit type is already encountered, increment its count

#             count = 0  # Initialize the count of total fruits collected
#             for _, v in num_fruits.items():  # Iterate through the dictionary items to get the count of each fruit
#                 count += v  # Increment the total count of fruits by the count of each fruit type
#             max_trees = max(count, max_trees)  # Update the maximum number of trees collected

#         return max_trees  # Return the maximum number of trees that can be collected

# baskets = Solution()  # Create an instance of the Solution class
# fruits = [3,3,3,1,2,1,1,2,3,3,4]  # Example list of fruits
# print(baskets.totalFruit(fruits))  # Print the maximum number of trees that can be collected

# #5 comes from 1,2,1,1,2

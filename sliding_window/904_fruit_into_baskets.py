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


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_trees = 0
        for i in range(len(fruits)):
            num_fruits = {}
            fruit_types = 0
            for j in range(i, len(fruits), 1):

                if fruits[j] not in num_fruits:
                    fruit_types += 1
                    if fruit_types > 2:
                        break
                    num_fruits[fruits[j]] = 1
                else:
                    num_fruits[fruits[j]] += 1

            count = 0
            for _, v in num_fruits.items():
                count += v
            max_trees = max(count, max_trees)

        return max_trees

baskets = Solution()
fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(baskets.totalFruit(fruits))

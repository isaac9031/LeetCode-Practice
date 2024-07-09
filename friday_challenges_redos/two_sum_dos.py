# def twoSum(numbers: list[int], target: int) -> list[int]:
#     #use pointers to go over the array
#     lp = 0
#     rp = len(numbers)-1
#     while lp<rp: #will keep track of rp
#         total = numbers[lp] + numbers[rp]
#         if total == target:
#             return [lp+1,rp+1]
#         elif total > target:
#             rp-=1
#         else:
#             lp+=1

# numbers = [2,7,11,15]
# target = 9
# print(twoSum(numbers, target))



class Solution(object):
    def twoSum(self, nums, target):



numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))



def increment(n):
    n[0] += 1

num = [10]  # Using a list to emulate pass by reference
print("Before increment:", num[0])
increment(num)
print("After increment:", num[0])

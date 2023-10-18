# class Solution():
#     def searchMatrix(self, matrix: list[list[int]], target)-> bool:
#         print(len(matrix))
#         for i in range(len(matrix)):
#             print(matrix[i])
#             if target in matrix[i]:
#                 return True
#         return False

# solution = Solution()
# matrix = [[1,2,5,7],[10,11,16,20],[23,30,3,60]]
# target = 3
# result =  solution.searchMatrix(matrix, target)
# print(result)

class Solution():
    def searchMatrix(self, matrix: list[list[int]], target)-> bool:
        print(len(matrix))
        for row in matrix:
            if target in row:
                return True
        return False

solution = Solution()
matrix = [[1,2,5,7],[10,11,16,20],[23,30,3,60]]
target = 3
result =  solution.searchMatrix(matrix, target)
print(result)

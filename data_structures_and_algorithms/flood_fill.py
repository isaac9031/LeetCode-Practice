class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        newlist  = []
        for lista in image:

            for inner_l in lista:
                print(lista[inner_l])
                if lista[inner_l]!= image[sr][sc]: #will be image[1][1]
                    new = inner_l*color
                    newlist.append(new)
        pass



solution = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, color = 1, 1, 2
result = solution.floodFill(image, sr, sc, color)

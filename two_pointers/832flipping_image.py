# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].

# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

#Using pointer
def flipAndInvertImage( image: list[list[int]]) -> list[list[int]]:
    #Make L and R pointers to swap the numbers for flipping by starting at the beginning and at the end of each list in the array
    for i in range(len(image)): # will start at list 0
        tempL = 0 #start at index 0 all the time since its always a new list
        print(len(image[i])-1)
        tempR = len(image[i])-1 #point to the last element on that specific list, this one 2
        middleOne = len(image)//2
        if image[i][middleOne] == 0:
            image[i][middleOne] = 1
        else:
            image[i][middleOne] =0

        while tempL < tempR:
            image[i][tempL],image[i][tempR] = image[i][tempR],image[i][tempL]
            if image[i][tempL] == 0:
                image[i][tempL] = 1
            else:
                image[i][tempL] = 0
            if image[i][tempR] == 0:
                image[i][tempR] = 1
            else:
                image[i][tempR] =0

            tempL +=1 #now it will be 1
            tempR -=1 # will also be one, therefore no more swapping after tempR == tempL


    return image

    #invert them by having an if statement for each element in each list at the end


image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))

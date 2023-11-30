
#Make it return this
# [[0,1], [2,3], [4,5]]

def partition(lista, size):
    #need to make the length of an array the same as the size that it is requiring
    fullList = []
    chunk = []
    i = 0
    while i < len(lista):
        if len(chunk)<size:
            chunk.append(lista[i]) #adding numbers to the chunk
        if len(chunk)== size: #now it checks to see if the chunk is the size we want, and it resets the chunk list
            fullList.append(chunk) #adding the whole list to fullList
            chunk = []
        i+=1
    return fullList


input = [0, 1, 2, 3, 4, 5, 6]

result = partition(input, 2)
print(result)

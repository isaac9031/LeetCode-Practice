class Solution(object):
    def replaceElements(self, arr):
        new_List = []
        for num in range(len(arr)-1):
            max_N = arr[num+1]
            for n_left in range(num+1,len(arr)-1):
                if max_N < arr[n_left]:
                    max_N = arr[n_left]
            new_List.append(max_N)
        new_List.append(-1)
        return new_List





solution = Solution()
arr = [17,18,5,4,6,1]
result = solution.replaceElements(arr)
print(result)
#start with a max_N tha is the first number to the right of the element we are on
#check to see which number is greater to the right, then adds that number to the list
#need to only list the numbers left on the right of the current one

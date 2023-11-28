def rearrangeArray(nums: list[int]) -> list[int]:
    #make two pointers to place values in the new lista
    #use a for loop to go over the nums list
    #use one if loop for positive and one for negative to store in lista
    #pointer l starts at 0 and increments by 2, pointer m starts at 1 and also increments by 2
    lista = len(nums)*[0]
    l = 0
    m = 1
    for i in range(len(nums)):
        if nums[i] > 0:
            lista[l] = nums[i]
            l+=2
        if nums[i] < 0:
            lista[m] = nums[i]
            m+=2
    return lista


nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))

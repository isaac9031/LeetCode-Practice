# def productExceptSelf(nums: list[int]) -> list[int]:
#     pre = 1
#     post = 1
#     listapre = [1]
#     listapost = [1]
#     final = []

#     for i in range(len(nums)):
#        pre *= nums[i]
#        listapre.append(pre)
#     for i in range(len(nums)-1,-1,-1):
#        post *= nums[i]
#        listapost.append(post)

#     for i in range(len(nums)):
#        final.append(listapre[i]*listapost[-i-2])
#     return final
#     print(listapre,listapost)
#     print(final)




# nums = [1,2,3,4]
# print(productExceptSelf(nums))


#restrictions from the problemL: we cannot use division, and it has to run on O(n)



#Method online
def productExceptSelf(nums: list[int]) -> list[int]:
    res = [1] * (len(nums)) #will form a list of  res = [1, 1, 1, 1]
    prefix = 1  #we will start with a value of 1

    for i in range(len(nums)):
        res[i] = prefix  #indx 0 will be value 1; indx 1,1 ; indx 2,2; indx3, 6
        prefix *= nums[i] 
    #end up with res = [1, 1, 2, 6], the last three elements are the prefix, we don't need the last value of 24
    post = 1
    for i in range(len(nums)-1,-1,-1): #will start from the end, index 3 and go backwards by 1
        res[i] *= post #indx 3, which is 6*1; indx 2 which is 2*4=8 ; indx 1 which is 1*12; indx0, 1*24
        post *= nums[i]
        print(post)
    return res
    #end up with res = [24, 12, 8, 6]

nums = [1,2,3,4]
print(productExceptSelf(nums))

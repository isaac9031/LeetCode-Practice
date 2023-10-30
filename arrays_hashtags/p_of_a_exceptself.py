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
    res = [1] * (len(nums))
    prefix = 1

    for i in range(len(nums)):
        res[i] = prefix
        print(res[i])
        prefix *= nums[i]
        print(prefix)
    post = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= post
        print(res[i])
        post *= nums[i]

    return res

nums = [1,2,3,4]
print(productExceptSelf(nums))

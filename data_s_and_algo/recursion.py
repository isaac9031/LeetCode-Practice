def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)


print(fact(5))

# 5 * fact(4)  = 5*24 =120 ; return 120 for fact(5)
# 4 * fact(3)  = 4*6  = 24 ; return 24 for fac(4)
# 3 * fact(2)  = 3*2  = 6  ; return 6 for fact(3)
# 2 * fact(1)  = 2*1  = 2  ; return 2 for fact(2)
# 1    will give us     1  ; returns 1 for fact(1)

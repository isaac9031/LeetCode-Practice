
## Pass by reference
# When a parameter is passed the memory location
# originally referred to by the actual parameter is passed to the formal paramet
def increment(n):
    print(n)
    n[0] += 1  #10+=1

num = [10]  # Using a list to emulate pass by reference
print("Before increment:", num[0])
print(num)
increment(num)
print("After increment:", num[0])


#pass by value
# When a parameter is passed, any changes made to the formal parameter do NOT affect the actual parameter.
def increment(n):
    n += 1


num = 10
print("Before increment:", num)
increment(num) #we need to call function in the bottom print in order to get 11 since the value needs to be returned
#will not call the function, therefore there will be not changes and will stay as 10
print("After increment:", num)

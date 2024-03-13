#it multiplies everything in the list.
#if number list is 0, then it just skips the for loop
#and return 1
def multiply_all(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total

print(multiply_all([3, 4, 5, 6]))


#we need to multiply the values of height and width
def sum_areas(rectangles):
    total = 0
    for i in rectangles:
        total += i.get("height")*i.get("width")
    return total

rectangles = [
    {"height": 10, "width": 10},
    {"height": 12, "width": 12}
]
print(sum_areas(rectangles))

###############################################

#Returns the longest inner list
def find_longest(lists):
    biggest = []
    if len(lists) == 0 :
        return None
    else:
        for i in lists:
            if len(i)>len(biggest):
                biggest = i
        return biggest

lists= [[1], [1,2,3], [1,2]]
print(find_longest(lists))

#or
def find_longest(lists):
    if len(lists) == 0 :
        return None
    index_of_longest = 0
    for idx, list in enumerate(lists):
        if len(list) > len(lists[index_of_longest]):
            index_of_longest = idx
    return lists[index_of_longest]

lists= [[1], [1,2,3], [1,2]]
print(find_longest(lists))

######################################################

############
#missed this one, if numerator is integer then it return True
#if the quotient is not 0 then it returns False
def divides_evenly(numerator, denominator):
    if denominator == 0:
        return False
    quotient = numerator /denominator
    # if int(quotient) == quotient:
    #     return True
    # else:
    #     return False
    return int(quotient) == quotient




print(divides_evenly(6, 1.5))
print(divides_evenly(6, 2))
print(divides_evenly(6, 3))
print(divides_evenly(6, 4))
###############
##############################-------
#GOT THIS ONE WRONG, LOOK OVER IT AGAIN
#it will count delimeters, such as ",", "#",

def count_entries(line, separator):
    return len(line.split(separator))

print(count_entries("", " "))
print(count_entries("a", ","))
print(count_entries(",", ","))
print(count_entries("a,b,c", ","))
print(count_entries("a,b,c", ":"))

#we used this to solve the count problem above
print("a,b,c".split(","))
print(len("a,b,c".split(",")))

print("a,b,c".split(":"))
print(len("a,b,c".split(":")))
#################################--------


# takes a list of items and removes duplicates

def unique_elements(items):
    unique = {}
    for item in items:
        unique[item] = 1
    return list(unique.keys())

print(unique_elements([1,1,1]))

####Also missed the bottom one
#we ue type function
def add(items):
    sum = 0
    for item in items:
        sum += float(item)
    return sum

print(add(items))

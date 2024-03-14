# You are given:
# • n: the size of the array
# • val1: an integer
# • arr: an array of integers
# Write a function that takes the array arr, its size n, and the integer vall as input and returns an array containing the count of integers that are smaller than, equal to, and greater than val1, respectively.
# Example:
# Input:
# • n = 5
# • val1 = 6
# • arr = 246810
# Output:
# • 212
# Explanation:
# • In the given example, there are two integers smaller than 6(2 and 4), one integer equal to 6, and two integers greater than 6 (8 and 10).

# If input given by myself#
def countIntegers(n, val, arr):
	#create a new list
	#loop over the arr and compare each element to the value
	#make three variables to store less than, equal, and greater
	#todo: optimize solution
	less, equal, greater = 0, 0, 0
	for n in arr:
		if n<val:
			less+=1
		elif n == val:
			equal+=1
		else:
			greater+=1

	return f"{less} {equal} {greater}"

n=5
val1 = 6
arr = [2,4,6,8, 10]
print(countIntegers(n,val1,arr))

# IN TESTGORILLA platform each variable has an input from the outside(which always comes as a string so we need to convert the desired type)
def countIntegers(n, val, arr):
    smaller = sum(1 for num in arr if num < val)
    equal = sum(1 for num in arr if num == val)
    greater = sum(1 for num in arr if num > val)
    return [smaller, equal, greater]

n = int(input("Enter the length of the array: "))
val = int(input("Enter the value to compare against: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split())) #string "10 4 6 2 12 8 9" converted to a list ["10", "4", "6", "2", "12", "8", "9"]

result = countIntegers(n, val, arr)
print(' '.join(map(str, result)))

#NOTES OF HOW THE CODE WORKS
# arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
 #first converted to a list ["10", "4", "6", "2", "12", "8", "9"] by .split() , split() separate by white spaces by default, but you can change it. ex. 10-4-6-2-12-8-9 will require list.split("-")
#then map will apply the built in func int to every element on the list, therefore converting it to a list of integers



# print(' '.join(map(str, result)))
# first map will make each integer elemnt in the list "[smaller, equal, greater]" to a string
# then ' '.join will convert the whole list to a string

# ex. it will return [3, 1, 3]
# map will apply str function to each so now we will have ["3", "1", "3"]
# then ' '.join will convert the list into a str type and will have a space between each element 3 1 3

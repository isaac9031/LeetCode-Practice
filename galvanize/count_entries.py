# This function count_entries will take a string that's composed of values that are
# separated by some "delimiter" character, like a comma. It then returns the number of values in that string
# that are separated by the provided delimiter.


def count_entries(line, separator):
    if len(line) == 0 or len(line) == 1 or separator not in line:
        return 1
    if len(line) == 1:
            return 2
    lista = line.split(separator)
    total = 0
    for item in lista:
         if item != separator:
              total+=1
    return total

line = "a,b,c"
separator = ":"
print(count_entries(line, separator))




#16 digits to strings
def join_numbers(digits):
     string = ""
     for n in digits:
          string+=str(n)
     return "".join(string)


input = [3, 2, 1]
print(join_numbers(input))

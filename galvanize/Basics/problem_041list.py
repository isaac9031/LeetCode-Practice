# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.

def add_csv_lines(csv_lines):
    new = []
    total = 0
    total_each = []
    for i in csv_lines:
        new.append(i.split(","))        #splits the list into two lists [["8,1,7"], ["10,10,10"]]
        print(new)
    for i in new:                      # acces only one list at the time
        for x in i:                     #access within each list
            total += int(x)             #converts the str to integer. ex "8" to 8, then adds it to total of that specific list
        total_each.append(total)           #adds the total to total_each list
        total = 0                   #resets total to zero
    return total_each

print(add_csv_lines(["8,1,7", "10,10,10"]))

# Finding All substrings Frequency in String Using Python
#o(3) time complexity
def find_substring_frequencies_naive(string):
   substr_freq = {}
   n = len(string)

   # Generate all possible substrings
   for i in range(n):
      for j in range(i, n):
         substring = string[i:j + 1]
         # Count the occurrences of each substring
         if substring in substr_freq:
            substr_freq[substring] += 1
         else:
            substr_freq[substring] = 1

   return substr_freq


string = "banana"
naive_frequencies = find_substring_frequencies_naive(string)
print(naive_frequencies)

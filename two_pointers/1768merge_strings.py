# You are given two strings word1 and word2. Merge the strings by adding letters in alternating
# order, starting with word1. If a string is longer than the other, append the additional
# letters onto the end of the merged string.
# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

def mergeAlternately(word1: str, word2: str) -> str:
    #we will always start with the first letter of word1
    #use the length of the second one with an if statement that will just add the rest of
    #...the letters if it is greater than the first word. add one and one of each letter
    w1 = len(word1)
    w2 = len(word2)
    if w1<w2:
        n = w1
    else:
        n = w2
    l = 0
    mergedS = ""
    while l<n: # we try to get the shortest length so it stops adding one of each
        mergedS+=word1[l]
        mergedS+=word2[l]
        l+=1
    if n == w1: #we add the rest of the char from the longest word
        mergedS+=word2[l:]
    if n == w2:
        mergedS+=word1[l:]
    return mergedS

word1 = "abcd"
word2 = "pq"
print(mergeAlternately(word1, word2))

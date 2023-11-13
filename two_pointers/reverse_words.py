def reverseWords( s: str) -> str:
    new = s.split(" ")
    newlista = []
    for string in new:
        newlista.append(string[::-1])

    return (" ").join(newlista)



s = "Let's take LeetCode contest"
print(reverseWords(s))

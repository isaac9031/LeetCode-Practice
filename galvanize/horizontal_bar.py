def horizontal_bar_chart(sentence):
    lista = [] #need to return a list
    letterN = {}
    sentence = sorted(sentence)
    for l in sentence: #need to go over string
        if l != " ":
            if l not in letterN:
                letterN[l] = 0
            letterN[l] +=1
    #will get {letter:#of times its in the array}
    for key, value in letterN.items():
        lista.append(key*value)
    return lista

sentence = "abba has a banana"
print(horizontal_bar_chart(sentence))



#how Galvanize did it:
# def horizontal_bar_chart(sentence):
#     d = {}
#     for c in sentence:
#         if c >= "a" and c <= "z":
#             if c not in d:
#                 d[c] = ""
#             d[c] += c
#     result = []
#     for s in d.values():
#         result.append(s)
#     return list(sorted(result))

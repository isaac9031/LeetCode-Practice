def isPangram(pangram):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters = set(pangram.lower())
    return alphabet.issubset(letters)

def check_sentence(pangram):
    if isPangram(pangram):
        print("is a pangram")
    else:
        print("this is not a pangram")


sentence = "The quick brown fox jumps over the lazy dog"
check_sentence(sentence)

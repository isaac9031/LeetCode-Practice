# Complete the make_sentences function that accepts three
# lists.
#   * subjects contains a list of subjects for three-word sentences
#   * verbs contains a list of verbs for three-word sentences
#   * objects contains a list of objects for three-word sentences
# The make_sentences function should return all possible sentences
# that can be made from the words in each list
#
# Examples:
#   * subjects: ["I"]
#     verbs:    ["play"]
#     objects:  ["Portal"]
#     returns:  ["I play Portal"]
#   * subjects: ["I", "You"]
#     verbs:    ["play"]
#     objects:  ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "You play Portal", "You play Sable"]
#   * subjects: ["I", "You"]
#     verbs:    ["play", "watch"]
#     objects:  ["Portal", "Sable"]
#     returns:  ["I play Portal", "I play Sable",
#                "I watch Portal", "I watch Sable",
#                "You play Portal", "You play Sable"
#                "You watch Portal", "You watch Sable"]
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def make_sentences(subjects, verbs, objects):
    new_list = []
    for i in subjects:
        for x in verbs:
            for y in objects:
                new_list.append(i+" "+x+" "+y)
    return new_list



print(make_sentences(["I", "You"],["play"],["Portal", "Sable"]))

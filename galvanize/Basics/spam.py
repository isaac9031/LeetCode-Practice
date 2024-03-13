# def getSpamEmails(subjects, spam_words):
#     spamornot = []

#     for subject in subjects:
#         words = subject.lower().split()
#         spam_count = 0
#         for word in spam_words:
#             spam_count += words.count(word.lower())
#             if spam_count >= 2:
#                 spamornot.append("spam")
#                 break
#         else:
#             spamornot.append("not_spam")
#     return spamornot

def getSpamEmails(subjects, spam_words):
    spamornot = []

    spam_words_set = set(word.lower() for word in spam_words)

    for subject in subjects:
        words = (word.lower() for word in subject.split())
        spam_count = sum(1 for word in words if word in spam_words_set)
        if spam_count >= 2:
            spamornot.append("spam")
        else:
            spamornot.append("not_spam")
    return spamornot

subjects = ["i paid him paid", "summertime sadness"]
spam_words = ["i", "sadness", "paid"]

print(getSpamEmails(subjects, spam_words))

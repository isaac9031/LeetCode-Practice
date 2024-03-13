# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"



def check_password(password):
    lower_case = 0
    upper_case = 0
    digit = 0
    special = "$,!,@"
    special_character= 0
    if len(password) >= 6 and len(password) <= 12:
        for i in password:
            if i.isdigit():
                digit += 1
            if i.isupper():
                upper_case+=1
            if i.islower():
                lower_case+=1
            if i in special:
                special_character+=1
        if (digit>=1 and  upper_case>=1 and lower_case>=1 and special_character>=1):
            return print("Valid Password")
        else:
            return print("Invalid")
    else:
        return print("Invalid")


print(check_password("Aa93sssssss"))

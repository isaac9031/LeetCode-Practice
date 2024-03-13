# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_make_pasta(ingredients):
    pasta = []
    for ingredient in ingredients:
        if ingredient == "flour" or ingredient == "eggs" or ingredient == "oil":
            pasta.append(ingredient)
            if len(pasta) == 3:
                return True
            else:
                False



print(can_make_pasta(["flour", "oil", "tortillas", "oil"]))

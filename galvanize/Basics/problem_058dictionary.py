# Write a function that meets these requirements.
#
# Name:       group_cities_by_state
# Parameters: a list of cities in the format "«name», «st»"
#             where «name» is the name of the city, followed
#             by a comma and a space, then the two-letter
#             abbreviation of the state
# Returns:    a dictionary whose keys are the two letter
#             abbreviations of the states in the list and
#             whose values are a list of the cities appearing
#             in that list for that state
def group_cities_by_state(cities):          # solution
    output = {}                             # solution
    for city in cities:
        name, state = city.split(",")       #returns ("Cleveland", "OH") only works on strings and splits it into two
        state = state.strip()               # returns OH without the empty space on the left
        if state not in output:             # looks to see if there is no OH in the  output,
                                            #if there is then it goes to the next line of code, if not then it.....
            output[state] = []              # .....adds state key,OH, which will have a list as a value
        output[state].append(name)          # it adds/append a value to the list that was started in the previous step
    return output




print(group_cities_by_state(["Cleveland, OH", "Columbus, OH", "Chicago, IL"]))


# In the items in the input, there will only be one comma.
#
# Examples:
#     * input:   ["San Antonio, TX"]
#       returns: {"TX": ["San Antonio"]}
#     * input:   ["Springfield, MA", "Boston, MA"]
#       returns: {"MA": ["Springfield", "Boston"]}
#     * input:   ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
#       returns: {"OH": ["Cleveland", "Columbus"], "IL": ["Chicago"]}
#
# You may want to look up the ".strip()" method for the string.

def group_cities_by_state(cities):
    dictionary = {}

    for together in cities:
        city, state = together.split(",")
        state = state.strip()
        if state not in dictionary:
            dictionary[state] = []
        dictionary[state].append(city)
    return dictionary


print(group_cities_by_state(["Cleveland, OH", "Columbus, OH", "Chicago, IL"]))




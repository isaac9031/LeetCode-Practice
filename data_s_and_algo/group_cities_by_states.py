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
#
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
    dict_by_state = {}
    for city_state in cities:
        print(city_state.split(","))
        city, state = city_state.split(",") # converts strings to lists, then using ciy, state saves the string 1 in city and string 2 in state
        state = state.strip(" ")
        print(state)
        print(city)
        # print(type(state))=str
        print(city,state)
        if state not in dict_by_state:
            dict_by_state[state] = []
        dict_by_state[state].append(city)
    return dict_by_state

print(group_cities_by_state(["Cleveland, OH", "Columbus, OH", "Chicago, IL"]))

#                                              city       state
# with .split it will make it into a list...['Cleveland', ' OH']
# then .strip(" ") eliminates white spaces..['Cleveland', 'OH']
# In the first loop ['Cleveland', 'OH'] it will check IF the state is not in the dictionary
#since its not then it will add it to the dict_state by dict_state[state] = [], then right after...
#..if the state already is in the dictionary it will add the city to its correct state by  dict_state[state].append(city)

# will keep doing the same thing on the second loop >> ['Columbus', " OH']    ...third loop >> ['Chicago', 'IL]

#will return 1 since in the last dic {"background": "yellow", "size": 5,  "weight": "light"},
#.. there is no color so item.get("color") return None which equals None
# def count_matches(items, param2=None):
#     matches = []
#     for item in items:
#         if(item.get("color") == param2):
#             matches.append(item)
#     return len(matches)

# input = [
#     {"background": "green",  "size": 5,  "color": "blue"},
#     {"background": "yellow", "size": 5,  "color": "green"},
#     {"background": "blue",   "size": 25, "color": "green"},
#     {"background": "yellow", "size": 5,  "weight": "light"},
# ]

# result = count_matches(input)
# print(result)


def count_matches(items, match):
    matches = []
    for item in items:
        if(item.get("background") == match):
            matches.append(item)
    return len(matches)

input = [
    {"background": "green", "color": "blue", "size": 5},
    {"color": "green", "size": 5, "weight": "heavy"},
    {"background": "yellow", "size": 5,  "weight": "light"},
    {"color": "blue", "size": 25, "weight": "light"},
]

result = count_matches(input, None)
print(result)

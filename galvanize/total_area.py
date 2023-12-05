# This function takes a list of rectangles described by their heights and widths. It sums up the areas of all of the rectangles.
# Here's an example input for the sum_areas function with one rectangle description in it:

def sum_areas(rectangles):
    total = 0
    for rectangle in rectangles:
        total += rectangle["height"]*rectangle["width"]
    return total

rectangles = [
    {"height": 10.5, "width": 0},
    {"height": 0, "width": 8},
    {"height": 10, "width": 10},
    {"height": 12, "width": 12}
]

print(sum_areas(rectangles))

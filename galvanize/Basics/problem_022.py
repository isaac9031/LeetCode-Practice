# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    gear_needed = []
    if is_workday == "yes" and is_sunny == "no":
        gear_needed.append("umbrella")
        gear_needed.append("laptop")
        return gear_needed
    elif is_workday == "no" and is_sunny == "yes":
        gear_needed.append("surfboard")
        return gear_needed

print(gear_for_day("yes", "no"))

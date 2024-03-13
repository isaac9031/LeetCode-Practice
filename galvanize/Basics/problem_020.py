# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def quorum(member, attendees):

    if (len(attendees)) >= len(member)*.5:
        print("More than 50% attended")
    else:
        print("less than 50% attended")

print(quorum(["a", "b", "c", 'd'], ["a", "b", "c"]))

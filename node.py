# know that a node carries a value and can connect to one or more other nodes.

class Node:

    def __init__(self, value, link=None):
        self.value = value
        self.link = link

    def __str__(self):

        return ("Node { value: '" + str(self.value)
                + "', link: " + str(self.link) + " }")
# Python
x = Node(5) #not linked to the list

#adding t = Node("air") so it will be used to point to the root Node, then t will become the new root Node
t = Node("air")

p = Node("paper")
r = Node("rock")
s = Node("scissors")

t.link = p #we now make t the parent of p
p.link = r  # p will be the parent of r and both will be connected
r.link = s # r will be the parent of s and both will be connected
# print(x)
# print(x.value)

# New value for x
x.value = 10
# print(x.value)
# print(p.value, r.value, s.value)
print(p.link)
print(p)

#now t is the parent of p.
print(t)

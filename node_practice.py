
#Node class in which init function starts the node with the data passed as an argument.
#reference is None because if we only have one Node then there is nothing to reference

#Operations: get_size(), find(data), add(datat), remove(data)

class Node:
    def __init__(self, data, n = None): #constructor will take a piece of data and the next Node in
        self.data = data
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data (self, d):
        self.data = d

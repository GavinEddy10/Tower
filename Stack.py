
class Stack:

    def __init__(self, name=None, limit=None, top_item=None):
        self.name = name
        self.top = top_item
        self.size = 0
        self.limit = 40000 #change to limit = limit
        if self.top is not None and limit > 1:
            self.size += 1

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def peek(self):
        return self.top

    def push_n(self, node):
        if not self.has_space():
            print("Stack Full")
            return
        node.set_next_node(self.top)
        self.top = node
        self.size += 1

    def push_v(self, value):
        if not self.has_space():
            print("Stack Full")
            return
        n = Node(value)
        n.set_next_node(self.top)
        self.top = n
        self.size += 1

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.size < self.limit

    def pop(self):
        if self.size == 0:
            print("Stack empty")
            return
        pop = self.top
        self.top = self.top.get_next_node()
        pop.set_next_node(None)
        self.size -= 1
        return pop

    def print_stack(self):
        if self.size == 0:
            print("T {} B")
            return
        current = self.top
        print("T ", end="")
        for i in range(self.size):
            current.to_string()
            current = current.get_next_node()
        print(" B")


class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value
    def to_string(self):
        if self.get_next_node() is None:
            print("{ val: " + str(self.value) + " }", end="")
            return
        print("{ val: " + str(self.value) + " } ", end="")


class List:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

        def __str__(self):
            return f"{str(self.val)}{','+str(self.next) if self.next else ''}"

    def __init__(self):
        self.top = None

    def __str__(self):
        return f"[{str(self.top)}]"

    def add_first(self, val):
        node = self.Node(val)
        node.next, self.top = self.top, node

    def reverse(self):
        node = self.top
        new_top = None
        while node:
            node.next, new_top, node = new_top, node, node.next
        self.top = new_top

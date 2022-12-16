class List:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.top = None

    def __str__(self):
        node = self.top
        result = ''
        while node:
            result += str(node.val)
            if node.next:
                result += ','
            node = node.next
        return '['+result+']'

    def add_first(self, val):
        node = self.Node(val)
        node.next = self.top
        self.top = node

    def reverse(self):
        node = self.top
        tmp = None
        while node:
            node.next, tmp, node = tmp, node, node.next
        self.top = tmp

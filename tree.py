class Color:
    BLACK = 'BLACK'
    RED = 'RED'


class Tree:
    class Node:

        def __init__(self, val):
            self.left = None
            self.right = None
            self.color = None
            self.val = val

    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root:
            result = self.add_node(self.root, val)
            self.root = self.rebalance(self.root)
            self.root.color = Color.BLACK
            return result
        else:
            self.root = Tree.Node(val)
            self.root.color = Color.BLACK
            return True

    def add_node(self, node, val):
        if node.val == val:
            return False
        else:
            if node.val > val:
                if node.left is not None:
                    result = self.add_node(node.left, val)
                    node.left = self.rebalance(node.left)
                    return result
                else:
                    node.left = Tree.Node(val)
                    node.left.color = Color.RED
                    return True
            else:
                if node.right is not None:
                    result = self.add_node(node.right, val)
                    node.right = self.rebalance(node.right)
                    return result

                else:
                    node.right = Tree.Node(val)
                    node.right.color = Color.RED
                    return True

    @staticmethod
    def color_swap(node):
        node.right.color = Color.BLACK
        node.left.color = Color.BLACK
        node.color = Color.RED

    @staticmethod
    def left_swap(node):
        left_child = node.left
        middle_child = left_child.right
        left_child.right = node
        node.left = middle_child
        left_child.color = node.color
        node.color = Color.RED
        return left_child

    @staticmethod
    def right_swap(node):
        right_child = node.right
        middle_child = right_child.left
        right_child.left = node
        node.right = middle_child
        right_child.color = node.color
        node.color = Color.RED
        return right_child

    @staticmethod
    def rebalance(node):
        result = node
        while True:
            need_rebalance = False
            if (result.right is not None and result.right.color == Color.RED and
                    (result.left is None or result.left.color == Color.BLACK)):
                need_rebalance = True
                result = Tree.right_swap(result)

            if (result.left is not None and result.left.color == Color.RED and
                    result.left.left is not None and result.left.left.color == Color.RED):
                need_rebalance = True
                result = Tree.left_swap(result)

            if (result.left is not None and result.left.color == Color.RED and
                    result.right is not None and result.right.color == Color.RED):
                need_rebalance = True
                Tree.color_swap(result)
            if not need_rebalance:
                break
        return result


if __name__ == '__main__':
    my_tree = Tree()
    values = [13, 8, 17, 1, 11, 15, 25, 22, 6, 7]
    for i in values:
        my_tree.add(i)
    pass

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        from pprint import pformat
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({'%s' % (self.value): (self.left, self.right)}, indent=1)


class BinarySearchTree:
    def __init__(self, root=None):
        
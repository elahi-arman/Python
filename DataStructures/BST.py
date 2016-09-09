import copy

class BST(object):
    """
        Simple BST implementation in Python.
    """

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        str = "Value:  %d\t" % self.value
        if self.left is not None:
            str += "Left: %d\t" % self.left.value
        if self.right is not None:
            str += "Right: %d\t" % self.right.value

        return str

    def add(self, node):
        if (type(node) is BST):
            if self.value == node.value:
                print('Values are equal, could not add')
                return False
            if node.value < self.value:
                if self.left == None:
                    self.left = node
                    return True
                else:
                    self.left.add(node)
            elif node.value > self.value:
                if self.right == None:
                    self.right = node
                    return True
                else:
                    self.right.add(node)
        else:
            return False

    def search(self, value):
        if value == self.value:
            return copy.deepcopy(self)

        if value < self.value:
            if self.left is not None:
                return self.left.search(value)
            else:
                return None
        elif value > self.value:
            if self.right is not None:
                return self.right.search(value)
            else:
                return None


    def inOrderTraversal(self, fxn = print):

        if self.left is not None:
            self.left.inOrderTraversal(fxn)

        fxn(self.value)

        if self.right is not None:
            self.right.inOrderTraversal(fxn)

    def preOrderTraversal(self, fxn = print):

        fxn(self.value)

        if self.left is not None:
            self.left.preOrderTraversal(fxn)
        if self.right is not None:
            self.right.preOrderTraversal(fxn)

if __name__ == '__main__':
    bt = BST(50)
    bt.add(BST(25))
    bt.add(BST(75))
    bt.add(BST(30))
    bt.add(BST(12))
    bt.add(BST(100))

    bt.preOrderTraversal()
    print(bt.search(50))
    print(bt.search(25))
    print(bt.search(30))
    print(bt.search(100))
    print(bt.search(0))

    bt.preOrderTraversal()

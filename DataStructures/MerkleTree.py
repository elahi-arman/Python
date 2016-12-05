import BST

class MerkleTree(BST):

    def __init__(self, value, hashFunction):

        BST.__init__(self, value)
        self.hash = hashFunction
        self.hashedValue = self.hash(value)

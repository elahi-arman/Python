from node import Node

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def insertFront(self, node):
        if (self.head == None):
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.setNext(temp)

    def insertBack(self, node):
        self.tail.setNext(node)
        self.tail = self.tail.getNext()

    def printList(self):
        for node in self:
            print(node.getData())

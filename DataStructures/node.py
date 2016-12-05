class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def setNext(self, next):
        self.next = next

# Creating node class
class Node:
    def __init__(self,value=None):
        self.data  = value
        self.next = None
        self.prev = None

# creating diblelly linked list
class DoubleLL:
    def __init__(self):
        self.head = None

    # Inserting at the end
    def InsertAtEnd(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = temp
        temp.prev = t


    # print the LL
    def printDLL(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = DoubleLL()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtEnd(40)
obj.printDLL()


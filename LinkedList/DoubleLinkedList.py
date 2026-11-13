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


    # insert at the beginning
    def InsertAtBeg(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp


    # insert at middle
    def InsertAtMid(self,value,x):
        t = self.head
        while t.next is not None:
            if t.data is x:
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t


    # delete LL
    # def deletionDLL(self,value):
    #     if self.head is None:
    #         print("L L is empty")
    #         return
        
    #     t = self.head
    #     if t.data is value:
    #         self.head = t.next
    #         self.head.prev = None
    #         return
    #     while t.next is not None:
    #         if t.data is value:
    #             t.prev.next = t.next
    #             t.next.prev = t.prev
    #             return
    #     if t.data is value:
    #         t.prev.next = None
    def deletionDLL(self, value):
        if self.head is None:
            print("LL is empty")
            return

        t = self.head

    # Delete head node
        if t.data == value:
            self.head = t.next

        if self.head is not None:
            self.head.prev = None

        return

    # Search for the node
        while t is not None:

            if t.data == value:

            # Connect previous node to next node
                t.prev.next = t.next

            # Connect next node to previous node
            if t.next is not None:
                t.next.prev = t.prev

            return

        t = t.next

        print("Value not found")

    # print the LL
    def printDLL(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data, end=' <---> ')
            t1 = t1.next
        print(t1.data)

    

obj = DoubleLL()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtEnd(40)
obj.InsertAtBeg(5)
obj.InsertAtMid(15,10)
obj.InsertAtMid(25,20)
obj.InsertAtMid(35,30)
obj.deletionDLL(25)
obj.printDLL()


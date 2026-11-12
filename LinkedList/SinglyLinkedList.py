class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head

    # Insert at beginning
    def InsertAtBeginning(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    # Insert at the end
    def InsertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 =  self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next  = temp
        else:
            self.head = temp

    # Insert at the middle
    def InsertAtMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next =  temp
            t1 = t1.next

    # Delete element
    def DeleteLL(self,value):
        # Empty LL
        if self.head is None:
            return

        t1 = self.head

        # delete first node
        if t1.data == value:
            self.head = t1.next
            return
        prev = None

        # search  for the node
        while t1 is not None:
            if t1.data == value:
                prev.next == t1.next
                return


            prev = t1
            t1 = t1.next





    # Print the element in LL
    def printLL(self):
        t1 = self.head
        while(t1 != None):
            print(t1.data)
            t1 = t1.next
        




obj = SinglyLinkedList()
obj.InsertAtBeginning(0)
obj.InsertAtEnd(10)
obj.InsertAtEnd(15)
obj.InsertAtMid(5,0)
obj.InsertAtEnd(20)
obj.InsertAtEnd(25)
obj.InsertAtEnd(30)
obj.DeleteLL(10)
obj.printLL()
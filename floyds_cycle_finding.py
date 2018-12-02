#firecode.io


class Node:
    def __init__(self):
        self.data = None
        self.next = None
     
    def setData(self,data):
        self.data = data
      
    def getData(self):
        return self.data
     
    def setNext(self,nextNode):
        self.next = nextNode
     
    def getNext(self):
        return self.next

class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    def is_cyclic(self):
        
        if self.head is None or self.head.next is None:
            return False
        slow_pointer = self.head
        fast_pointer = self.head.next
        
        
        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
          
        
        return False

if __name__ == "__main__":
    """
    Linked List: 3->5
    False
    Linked List: -1->-2->-3->-1
    True
    Linked List: 1
    False
    Linked List: 1->2->3->4->5->1
    True
    """
    n1 = Node()
    n1.setData(3)
    n2 = Node()
    n2.setData(5)
    n1.setNext(n2)
    singleLinkedList = SinglyLinkedList()
    singleLinkedList.setHead(n1)
    print("Linked List: 3->5")
    print(singleLinkedList.is_cyclic())


    n1 = Node()
    n1.setData(-1)
    n2 = Node()
    n2.setData(2)
    n1.setNext(n2)
    n3 = Node()
    n3.setData(3)
    n2.setNext(n3)
    n3.setNext(n1)
    print("Linked List: -1->-2->-3->-1")
    singleLinkedList = SinglyLinkedList()
    singleLinkedList.setHead(n1)
    print(singleLinkedList.is_cyclic())

    n1 = Node()
    n1.setData(1)
    singleLinkedList = SinglyLinkedList()
    singleLinkedList.setHead(n1)
    print("Linked List: 1")
    print(singleLinkedList.is_cyclic())
    
    n1 = Node()
    n1.setData(1)
    n2 = Node()
    n2.setData(2)
    n3 = Node()
    n3.setData(3)
    n4 = Node()
    n4.setData(4)
    n5 = Node()
    n5.setData(5)
    n1.setNext(n2)
    n2.setNext(n3)
    n3.setNext(n4)
    n4.setNext(n5)
    n5.setNext(n1)

    print("Linked List: 1->2->3->4->5->1")
    singleLinkedList = SinglyLinkedList()
    singleLinkedList.setHead(n1)
    print(singleLinkedList.is_cyclic())

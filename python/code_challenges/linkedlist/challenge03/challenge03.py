class Node:
    '''This is a class to define nodes'''
    def __init__(self, x):
         self.val = x
         self.next = None

class LinkedList:
    '''This is class to create linked list methods'''
    def __init__(self):
        self.head = None

    def append(self, node):
        '''This method is made to accept nodes and append them to the the linked list'''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        
        
    def deleteNthNode(self,head,n:int):
        '''A method that takes a head and n integer which refers to the node to be removed and
        using 2 pointers to iterate through the linked list when the second pointer reaches the end of the list the 
        first pointer should at the nth node to be removed'''
        firstPointer = head
        secondPointer = head
        firstPointerIndex = 0
        secondPointerIndex = 0
        while firstPointer is not None:
            firstPointer = firstPointer.next
            firstPointerIndex += 1
            if firstPointerIndex - secondPointerIndex > n + 1:
                 secondPointer = secondPointer.next
                 secondPointerIndex += 1
        if firstPointerIndex - secondPointerIndex <= n:
            return head.next
        secondPointer.next = secondPointer.next.next
        return head
    
    def printAll(self):
        '''this is a method to print the linked list values inside of a list'''
        elements=[]
        if self.head is None:
            return("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                elements.append(current.val)
                current = current.next
            return elements
            
             
SLL = LinkedList()
node1 = Node(4)
SLL.append(node1)

node2 = Node(9)
SLL.append(node2)

node3 = Node(5)
SLL.append(node3)

node4 = Node(1)
SLL.append(node4)

node5 =Node(7)
SLL.append(node5)
node6 = Node(3)
SLL.append(node6)

print(SLL.printAll())

#print(SLL.middleNode())
SLL.deleteNthNode(SLL.head,2)
print(SLL.printAll())
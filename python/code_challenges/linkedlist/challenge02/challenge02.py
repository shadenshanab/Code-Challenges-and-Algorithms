class Node:
    '''we define the nodes in this class'''

    def __init__(self, nodeValue):
        self.val = nodeValue
        self.next = None


class LinkedList:
    '''we create the linked list methods here'''

    def __init__(self):
        self.head = None

    def append(self, node):
        '''handle accept and append the nodes'''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def middleNode(self):
        '''Given the head of a singly linked list, return the middle node of the linked list.
        If there are two middle nodes, return the second middle node.
        Using two pointers—one to run to the end value and the other to catch the middle node
        when the first node reaches the end value—it iterates over the list.'''
        pointer = self.head
        mid_node = self.head
        while (pointer.next != None):
            pointer = pointer.next.next
            mid_node = mid_node.next
        return mid_node.val

    def printAll(self):
        '''This method prints the linked list values contained within a list.'''
        elements = []
        if self.head is None:
            return ("linked list is empty")
        else:
            current = self.head
            while current is not None:
                elements.append(current.val)
                current = current.next
            return elements


def deleteNode(node):
    '''This function deletes nodes that only have access to the node, and it takes into account the fact that the node is not a tail node.'''

    if not node:
        return

    node.val = node.next.val
    node.next = node.next.next


SLL = LinkedList()

node1 = Node(9)
SLL.append(node1)
node2 = Node(6)
SLL.append(node2)
node3 = Node(2)
SLL.append(node3)
node4 = Node(7)
SLL.append(node4)
node5 = Node(3)
SLL.append(node5)
node6 = Node(1)
SLL.append(node6)

deleteNode(node3)

print(SLL.printAll())

print(SLL.middleNode())

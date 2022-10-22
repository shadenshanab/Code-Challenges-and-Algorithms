# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value=value
        self.next= None

class linkedlist:
    def __init__(self):
        self.head=None

    def add_to_list(self,node):
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def delete_from_list(self,node):
        current=self.head
        if (current is not None):
            if (current.value == node):
                self.head = current.next

                return
        while(current is not None):
            if current.value == node:
                break
            prev = current
            current = current.next
        if current==None:
            print("Value not found")
            return ("Value not found") 

        prev.next = current.next
 
        current = None

    def print_list(self):
        if self.head is None:
            print("list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next

var1 = linkedlist()
var1.add_to_list('S')
var1.add_to_list('H')
var1.add_to_list('A')
var1.add_to_list('D')
var1.add_to_list('E')
var1.add_to_list('N')

var1.print_list()
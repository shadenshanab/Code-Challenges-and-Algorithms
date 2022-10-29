class Node:
    '''
    initialise nodes
    '''
    def __init__(self, vlaue):
        self.next = None
        self.value = vlaue


class Stack:
    '''
    make stack methods (push, peek , pop, get_size, and isEmpty).
    '''
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return ("This stack is empty")

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return ("This stack is empty")

    def isEmpty(self):
        return self.size == 0

    def get_size(self):
        return self.size


class Queue:
    '''
    initialise a queue built on two stacks
    '''
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        self.stack1.push(x)
 
    # pop element from the queue
    def pop(self):
 
        # if both the stacks are empty
        if self.isEmpty():
            print("This queue is empty")
            return
 
        # if stack2 is empty and stack1 has elements
        elif self.stack2.size == 0 and self.stack1.size > 0:
            while self.stack1.size:
                temp = self.stack1.pop()
                self.stack2.push(temp)
            return self.stack2.pop()
 
        else:
            return self.stack2.pop()

    def peek(self):
        """
        looks into the queue's first node
        """
        if self.isEmpty():
            return "This queue is empty"
        else:
            while self.stack1.size:
                self.stack2.push(self.stack1.pop())
            return self.stack2.peek()

    def isEmpty(self):
        """ "
        determines whether the stacks upon which the queue 
        is created are empty and then returns a boolean decision.
        """
        return self.stack1.size == 0 and self.stack2.size == 0


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)

    print(q.peek())

    print(q.isEmpty())
    
    print(q.pop())
    print(q.pop())
    print(q.pop())

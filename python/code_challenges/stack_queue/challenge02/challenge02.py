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


def is_valid(s):
    Parentheses={'(':')','{':'}','[':']'}
    stack=Stack()
    for i in s:
        if i in Parentheses.keys():
            stack.push(i)
        elif i in Parentheses.values():
            if stack.isEmpty():
                return False
            if Parentheses[stack.pop()]!=i:
                return False
    return stack.isEmpty()

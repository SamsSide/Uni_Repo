class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data
    
def postfix(x):
    S = Stack()
    for i in x:
        if i == "+":
            S.push(S.pop() + S.pop())
        elif i == "*":
            S.push(S.pop() * S.pop())
        elif i == "-":
            one = S.pop()
            two = S.pop()
            S.push(two-one)
        elif i == "/":
            one = S.pop()
            two = S.pop()
            S.push(two/one)
        else:
            S.push(int(i))
    return(S.top())

print(postfix("4512+-/"))
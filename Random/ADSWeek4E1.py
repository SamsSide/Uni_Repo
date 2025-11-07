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
    
def thirdRow(x):
    S = Stack()
    P = 0
    A = []
    for i in x:
        while S.isEmpty() == False and x[S.top()] <= i:
            S.pop()
        if S.isEmpty():
            A.append("*")
        else:
            A.append(P - S.top())
        S.push(i)
        P += 1
    return(A)

test = [221, 198, 203, 214, 213, 219, 220, 216, 218, 222]
print(thirdRow(test))
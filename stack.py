class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,element):
        self.stack.append(element)

    def is_empty(self):
        return len(self.stack)==0

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)  

mystack=Stack()

mystack.push('A')
mystack.push('B')
mystack.push('C')

print(f"My Stack is {mystack.stack}")

mystack.pop()

print(f"After poping the element my stack looks like {mystack.stack}")



print(f"Lets peek from my stack {mystack.peek()}")



print(f"Size of stack is :{mystack.size()} ")
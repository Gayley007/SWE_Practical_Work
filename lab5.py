# Implementing a Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  
print(stack.peek()) 
print(stack.size()) 

#Implementing a Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.front())  
print(queue.size())  

# Solving Practical Problems
"""Balanced Parenthesis"""
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

print(is_balanced("((()))")) 
print(is_balanced("(()")) 

'''Reverse a String'''
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

print(reverse_string("Hello, World!")) 

'''Hot Potato Simulation'''
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7)) 


#function that uses a stack to evaluate postfix expressions.
def evaluate_postfix(expression):
    stack = []  
    operators = set(['+', '-', '*', '/']) 
    for token in expression.split(): 
        if token not in operators:
            stack.append(float(token))  
        else:
            b = stack.pop() 
            a = stack.pop()
           
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack.pop()  

postfix_expression = "2 2 + 4 * 5 /"  
result = evaluate_postfix(postfix_expression)
print(result) 

#function that uses two stacks to implement a queue.
class Queue:
    def __init__(self):
        self.stack1 = []  
        self.stack2 = []  

    def enqueue(self, item):
        self.stack1.append(item)  

    def dequeue(self):
        if not self.stack2:  
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Queue is empty")  
        return self.stack2.pop()  

queue = Queue()
queue.enqueue(22)
queue.enqueue(12)
print(queue.dequeue())  
print(queue.dequeue())  


#queue to implement a basic task scheduler.
from collections import deque

class TaskScheduler:
    def __init__(self):
        self.queue = deque()  
    def add_task(self, task):
        self.queue.append(task) 
    def run_tasks(self):
        while self.queue:  
            task = self.queue.popleft() 
            print(f"Running: {task}") 

scheduler = TaskScheduler()
scheduler.add_task("do it 1")
scheduler.add_task("do it 2")
scheduler.add_task("do it 3")

print("Executing tasks...")
scheduler.run_tasks()  

# function that uses a stack to convert infix expressions to postfix.
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for token in expression.split():
        if token.isalnum():  
            output.append(token)
        elif token in precedence: 
            while (stack and stack[-1] != '(' and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token) 
        elif token == '(':
            stack.append(token)  
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() 

    while stack: 
        output.append(stack.pop())

    return ' '.join(output) 

infix_expression = "W * ( X + Y ) - Z"
postfix_expression = infix_to_postfix(infix_expression)
print(f"Postfix: {postfix_expression}")

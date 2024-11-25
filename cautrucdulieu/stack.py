from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print("Phần tử trên cùng:", stack.peek())  # Output: 15
stack.pop()
print("Kích thước ngăn xếp:", stack.size())  # Output: 2


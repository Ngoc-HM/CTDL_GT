
# Bài 1: Cài đặt Stack cơ bản
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Bài 2: Đảo ngược chuỗi sử dụng Stack
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str


# Bài 3: Kiểm tra ngoặc hợp lệ
def is_valid_parentheses(s):
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.push(char)
        elif char in mapping.keys():
            if not stack.is_empty() and stack.peek() == mapping[char]:
                stack.pop()
            else:
                return False
    return stack.is_empty()


# Bài 4: Chuyển đổi số thập phân sang nhị phân
def decimal_to_binary(n):
    stack = Stack()
    while n > 0:
        stack.push(n % 2)
        n //= 2

    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    return binary


# Bài 5: Duyệt biểu thức hậu tố
def evaluate_postfix(expression):
    stack = Stack()
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)
    return stack.pop()


# Bài 6: Kiểm tra chuỗi Palindrome
def is_palindrome(s):
    stack = Stack()
    for char in s:
        stack.push(char)

    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    return s == reversed_str


# Bài 7: Sắp xếp stack bằng stack khác
def sort_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        curr = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > curr:
            stack.push(temp_stack.pop())
        temp_stack.push(curr)
    return temp_stack


# Bài 8: Tìm phần tử lớn nhất trong Stack
class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.max_stack.is_empty() or item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        if not self.stack.is_empty():
            popped = self.stack.pop()
            if popped == self.max_stack.peek():
                self.max_stack.pop()
            return popped
        return "Stack is empty!"

    def get_max(self):
        if not self.max_stack.is_empty():
            return self.max_stack.peek()
        return "Stack is empty!"


# Bài 9: Tìm chiều cao tối đa của stack trong biểu thức hậu tố
def max_stack_height_postfix(expression):
    stack_height = 0
    max_height = 0

    for char in expression:
        if char.isdigit():
            stack_height += 1
        else:
            stack_height -= 1
            stack_height += 1  # Do một phép toán sẽ đẩy lại 1 kết quả vào stack
        max_height = max(max_height, stack_height)

    return max_height


# Bài 10: Giải bài toán tháp Hà Nội
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)



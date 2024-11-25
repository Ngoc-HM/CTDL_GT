
# Import các bài tập từ file stack_exercises
from python_stack_exercises import *

# Test Bài 1: Cài đặt Stack cơ bản
print("# Bài 1: Cài đặt Stack cơ bản")
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Phần tử trên cùng:", stack.peek())  # Output: 30
print("Lấy ra phần tử:", stack.pop())     # Output: 30
print("Ngăn xếp rỗng?", stack.is_empty()) # Output: False

# Test Bài 2: Đảo ngược chuỗi sử dụng Stack
print("\n# Bài 2: Đảo ngược chuỗi")
print(reverse_string("hello"))  # Output: "olleh"

# Test Bài 3: Kiểm tra ngoặc hợp lệ
print("\n# Bài 3: Kiểm tra ngoặc hợp lệ")
print(is_valid_parentheses("({[]})"))  # Output: True
print(is_valid_parentheses("({[})"))  # Output: False

# Test Bài 4: Chuyển đổi số thập phân sang nhị phân
print("\n# Bài 4: Chuyển đổi số thập phân sang nhị phân")
print(decimal_to_binary(233))  # Output: "11101001"

# Test Bài 5: Duyệt biểu thức hậu tố
print("\n# Bài 5: Duyệt biểu thức hậu tố")
print(evaluate_postfix("23*54*+"))  # Output: 26

# Test Bài 6: Kiểm tra chuỗi Palindrome
print("\n# Bài 6: Kiểm tra chuỗi Palindrome")
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False

# Test Bài 7: Sắp xếp stack bằng stack khác
print("\n# Bài 7: Sắp xếp stack bằng stack khác")
stack_to_sort = Stack()
for item in [3, 1, 4, 2]:
    stack_to_sort.push(item)
sorted_stack = sort_stack(stack_to_sort)
while not sorted_stack.is_empty():
    print(sorted_stack.pop(), end=" ")  # Output: 1 2 3 4

# Test Bài 8: Tìm phần tử lớn nhất trong Stack
print("\n\n# Bài 8: Tìm phần tử lớn nhất trong Stack")
max_stack = MaxStack()
max_stack.push(5)
max_stack.push(1)
max_stack.push(8)
max_stack.push(3)
print("Max:", max_stack.get_max())  # Output: 8
max_stack.pop()
print("Max sau khi pop:", max_stack.get_max())  # Output: 8

# Test Bài 9: Tìm chiều cao tối đa của stack trong biểu thức hậu tố
print("\n# Bài 9: Tìm chiều cao tối đa của stack")
print(max_stack_height_postfix("23*54*+"))  # Output: 2

# Test Bài 10: Giải bài toán tháp Hà Nội
print("\n# Bài 10: Giải bài toán tháp Hà Nội")
hanoi(3, "A", "C", "B")

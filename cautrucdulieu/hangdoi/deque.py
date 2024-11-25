from collections import deque

# Khởi tạo deque
dq = deque()

print("1. Khởi tạo deque rỗng:")
print(f"Deque hiện tại: {dq}\n")

# Thêm phần tử vào cuối deque
dq.append("A")
dq.append("B")
dq.append("C")
print("2. Thêm phần tử vào cuối deque:")
print(f"Deque sau khi thêm A, B, C: {dq}\n")

# Thêm phần tử vào đầu deque
dq.appendleft("X")
dq.appendleft("Y")
print("3. Thêm phần tử vào đầu deque:")
print(f"Deque sau khi thêm X, Y vào đầu: {dq}\n")

# Lấy phần tử từ đầu deque
removed_item = dq.popleft()
print("4. Lấy phần tử từ đầu deque:")
print(f"Phần tử được lấy ra: {removed_item}")
print(f"Deque sau khi lấy phần tử đầu: {dq}\n")

# Lấy phần tử từ cuối deque
removed_item = dq.pop()
print("5. Lấy phần tử từ cuối deque:")
print(f"Phần tử được lấy ra: {removed_item}")
print(f"Deque sau khi lấy phần tử cuối: {dq}\n")

# Kiểm tra phần tử đầu và cuối
print("6. Kiểm tra phần tử đầu và cuối:")
print(f"Phần tử đầu: {dq[0]}")
print(f"Phần tử cuối: {dq[-1]}\n")

# Xóa tất cả phần tử
dq.clear()
print("7. Xóa tất cả phần tử trong deque:")
print(f"Deque sau khi xóa hết: {dq}\n")

# Thêm lại các phần tử để minh họa đảo ngược
dq.extend(["1", "2", "3", "4"])
print("8. Thêm nhiều phần tử cùng lúc:")
print(f"Deque sau khi thêm: {dq}\n")

# Đảo ngược deque
dq.reverse()
print("9. Đảo ngược deque:")
print(f"Deque sau khi đảo ngược: {dq}\n")

# Đếm số lần xuất hiện của phần tử
dq.append("3")
count = dq.count("3")
print("10. Đếm số lần xuất hiện của phần tử:")
print(f"Deque hiện tại: {dq}")
print(f"Số lần phần tử '3' xuất hiện: {count}\n")

# Xoay vòng deque
dq.rotate(2)
print("11. Xoay vòng deque (2 bước về cuối):")
print(f"Deque sau khi xoay vòng: {dq}\n")

dq.rotate(-3)
print("12. Xoay vòng deque (-3 bước về đầu):")
print(f"Deque sau khi xoay vòng: {dq}\n")

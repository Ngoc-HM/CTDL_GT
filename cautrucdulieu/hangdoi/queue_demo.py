import queue

# Tạo hàng đợi FIFO
q = queue.Queue(maxsize=5)  # Hàng đợi có sức chứa tối đa là 5 phần tử

print("1. Khởi tạo hàng đợi rỗng:")
print(f"Hiện trạng hàng đợi: {'Rỗng' if q.empty() else 'Không rỗng'}\n")

# Thêm phần tử vào hàng đợi
q.put("A")
q.put("B")
q.put("C")
print("2. Thêm phần tử vào hàng đợi:")
print(f"Đã thêm A, B, C vào hàng đợi.")
print(f"Kích thước hàng đợi hiện tại: {q.qsize()}\n")

# Kiểm tra hàng đợi có đầy không
print("3. Kiểm tra hàng đợi có đầy không:")
print(f"Hàng đợi có đầy không? {'Có' if q.full() else 'Không'}\n")

# Lấy phần tử từ đầu hàng đợi
item = q.get()
print("4. Lấy phần tử từ đầu hàng đợi:")
print(f"Phần tử được lấy ra: {item}")
print(f"Kích thước hàng đợi sau khi lấy phần tử: {q.qsize()}\n")

# Kiểm tra hàng đợi có rỗng không
print("5. Kiểm tra hàng đợi có rỗng không:")
print(f"Hàng đợi có rỗng không? {'Có' if q.empty() else 'Không'}\n")

# Thêm thêm phần tử để minh họa hàng đợi đầy
q.put("D")
q.put("E")
q.put("F")
print("6. Thêm thêm phần tử vào hàng đợi:")
print(f"Kích thước hàng đợi hiện tại: {q.qsize()}")
print(f"Hàng đợi có đầy không? {'Có' if q.full() else 'Không'}\n")

# Xử lý khi hàng đợi đầy
try:
    q.put("G", timeout=1)  # Thử thêm phần tử vào hàng đợi đầy, chờ 1 giây
except queue.Full:
    print("7. Hàng đợi đầy, không thể thêm G vào.\n")

# Lấy tất cả phần tử ra khỏi hàng đợi
print("8. Lấy tất cả phần tử trong hàng đợi:")
while not q.empty():
    item = q.get()
    print(f"Đã lấy ra: {item}")

print(f"Hàng đợi hiện trạng: {'Rỗng' if q.empty() else 'Không rỗng'}\n")

# Thêm lại để minh họa hành vi chờ
q.put("H")
print("9. Minh họa hành vi chờ khi lấy phần tử:")
print("Đang lấy phần tử từ hàng đợi (sẽ bị chặn nếu rỗng)...")
item = q.get()  # Không có timeout, sẽ chờ mãi nếu hàng đợi rỗng
print(f"Đã lấy ra: {item}")

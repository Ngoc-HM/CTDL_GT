class Node:
    def __init__(self, data):
        self.data = data  # Dữ liệu của nút
        self.prev = None  # Con trỏ tới nút trước
        self.next = None  # Con trỏ tới nút sau

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Điểm bắt đầu của danh sách

    # Thêm nút mới vào cuối danh sách
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Nếu danh sách rỗng
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Duyệt đến nút cuối
                current = current.next
            current.next = new_node
            new_node.prev = current

    # In danh sách theo chiều thuận
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # In danh sách theo chiều ngược
    def display_backward(self):
        current = self.head
        while current and current.next:  # Duyệt đến nút cuối
            current = current.next
        while current:  # Quay ngược lại
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# Sử dụng
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward()  # Output: 10 -> 20 -> 30 -> None
dll.display_backward()  # Output: 30 -> 20 -> 10 -> None

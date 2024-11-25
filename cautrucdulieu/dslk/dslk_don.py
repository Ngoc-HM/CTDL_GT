class Node:
    def __init__(self, data):
        self.data = data  # Dữ liệu của nút
        self.next = None  # Con trỏ tới nút tiếp theo

class SinglyLinkedList:
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

    # In danh sách
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Sử dụng
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()  # Output: 10 -> 20 -> 30 -> None

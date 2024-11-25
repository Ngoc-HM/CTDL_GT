###
# 
# Đề bài: Xây dựng hệ thống quản lý đơn hàng cho nhà hàng
# Mô tả bài toán:
# Một nhà hàng cần một hệ thống quản lý đơn hàng đơn giản với các chức năng cơ bản như thêm đơn hàng, 
# hiển thị danh sách đơn hàng chờ, xử lý đơn hàng, và hủy đơn hàng. 
# Hệ thống này cần sử dụng cấu trúc dữ liệu hàng đợi để quản lý thứ tự xử lý đơn hàng. Hãy thực hiện các yêu cầu sau:
# ###

from collections import deque
import time

class Order:
    def __init__(self, order_id, customer_name, items):
        """
        Khởi tạo một đơn hàng mới.
        :param order_id: Mã đơn hàng (duy nhất).
        :param customer_name: Tên khách hàng.
        :param items: Danh sách các món ăn trong đơn hàng.
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.timestamp = time.time()  # Thời gian đặt hàng

    def __str__(self):
        """
        Trả về chuỗi mô tả đơn hàng.
        """
        return (f"Order ID: {self.order_id}, "
                f"Customer: {self.customer_name}, "
                f"Items: {', '.join(self.items)}, "
                f"Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.timestamp))}")

class RestaurantOrderSystem:
    def __init__(self):
        """
        Khởi tạo hệ thống quản lý đơn hàng với hàng đợi rỗng.
        """
        self.order_queue = deque()

    def add_order(self, order):
        """
        Thêm một đơn hàng vào hàng đợi.
        :param order: Đối tượng Order cần thêm.
        """
        self.order_queue.append(order)
        print(f"Đã thêm {order}")

    def cancel_order(self, order_id):
        """
        Hủy một đơn hàng dựa trên mã đơn hàng.
        :param order_id: Mã đơn hàng cần hủy.
        """
        for order in self.order_queue:
            if order.order_id == order_id:
                self.order_queue.remove(order)
                print(f"Đã hủy đơn hàng với mã {order_id}")
                print(f"Tên của đơn hàng đã hủy: {order.customer_name}")
                return
        print(f"Không tìm thấy đơn hàng với mã {order_id}")

    def view_pending_orders(self):
        """
        Hiển thị danh sách các đơn hàng chờ chế biến.
        """
        if not self.order_queue:
            print("Không có đơn hàng chờ.")
        else:
            print("Danh sách đơn hàng chờ:")
            for order in self.order_queue:
                print(order)

    def process_order(self):
        """
        Xử lý đơn hàng đầu tiên trong hàng đợi.
        """
        if not self.order_queue:
            print("Không có đơn hàng để xử lý.")
        else:
            order = self.order_queue.popleft()
            print(f"Đang chế biến {order}")
            # Giả lập thời gian chế biến
            time.sleep(2)
            print(f"Đã hoàn thành {order}")
            print(f"Thời gian hoàn thành {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

# Ví dụ sử dụng hệ thống
if __name__ == "__main__":
    system = RestaurantOrderSystem()

    # Thêm đơn hàng
    order1 = Order(1, "Nguyễn Văn A", ["Phở", "Trà đá"])
    order2 = Order(2, "Trần Thị B", ["Bún chả", "Nước ngọt"])
    order3 = Order(3, "Lê Văn C", ["Cơm gà", "Nước lọc"])
    order4 = Order(4, "Phạm Thị D", ["Bún bò", "Trà sữa"])

    system.add_order(order1)
    system.add_order(order2)
    system.add_order(order3)
    system.add_order(order4)


    # Xem danh sách đơn hàng chờ
    system.view_pending_orders()

    # viết code delay 2s
    time.sleep(1)
    # Xử lý đơn hàng
    system.process_order()

    # Hủy đơn hàng
    system.cancel_order(2)

    system.process_order()

    # Xem danh sách đơn hàng chờ sau khi hủy
    system.view_pending_orders()

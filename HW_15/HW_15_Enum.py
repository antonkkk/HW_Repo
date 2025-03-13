# 9. Enum
from enum import Enum


class OrderStatus(Enum):
    PENDING = "Заказ ожидает обработки"
    IN_PROGRESS = "Заказ готовится"
    READY = "Заказ готов"
    COMPLETED = "Заказ выдан"
    CANCELLED = "Заказ отменён"


class Order:
    def __init__(self, order_id, status=OrderStatus.PENDING):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status):
        if isinstance(new_status, OrderStatus):
            self.status = new_status
        else:
            print("Неверный статус!")

    def display_status(self):
        print(f"Статус заказа {self.order_id}: {self.status.value}")


order1 = Order(order_id=1)
order1.display_status()

order1.update_status(OrderStatus.IN_PROGRESS)
order1.display_status()

order1.update_status(OrderStatus.READY)
order1.display_status()


from lab03.base import Order
from datetime import datetime, timedelta
from lab04.interfaces import Printable, Comparable


class PhysicalOrder(Order, Printable, Comparable):
    """Физический заказ - реализует интерфейсы Printable и Comparable"""
    
    def __init__(self, name, email, id_order, order_amount, status, pin, delivery_address, delivery_weight):
        super().__init__(name, email, id_order, order_amount, status, pin)
        self.delivery_address = delivery_address
        self.delivery_weight = delivery_weight

    def calculate_shipping(self):
        if self.delivery_weight > 20:
            return self.delivery_weight * 100
        if 0 < self.delivery_weight <= 20:
            return 0
        
    def can_be_shipped(self):
        return self.status == "paid" and self.delivery_address is not None
    
    def can_be_returned(self):
        return self.status == "shipped"
    
    def calculate_total_cost(self):
        shipping = self.calculate_shipping()
        if shipping is None:
            shipping = 0
        return self.amount + shipping
    
    def get_delivery_deadline(self):
        if self.status == "shipped":
            return "В пути, ожидайте в течение 3-5 дней"
        elif self.status == "paid":
            return "Будет отправлен в течение 24 часов"
        elif self.status == "new":
            return "Оплатите заказ для расчета срока доставки"
        return "Заказ отменен"
    
    def to_string(self):
        """Реализация метода из интерфейса Printable"""
        return (f"Физический заказ #{self.id_order} | "
                f"Клиент: {self.name} | "
                f"Сумма: {self.amount} руб | "
                f"Вес: {self.delivery_weight} кг | "
                f"Статус: {self.status}")
    
    def compare_to(self, other):
        """Реализация метода из интерфейса Comparable - сравниваем по сумме"""
        if not isinstance(other, Order):
            raise TypeError(f"Невозможно сравнить с типом {type(other)}")
        
        if self.amount < other.amount:
            return -1
        elif self.amount > other.amount:
            return 1
        else:
            return 0
    
    def __str__(self):
        parent_str = super().__str__() 
        return (f"{parent_str}\n"
                f"Адрес доставки: {self.delivery_address}\n"
                f"Вес заказа: {self.delivery_weight}\n"
                f"Стоимость доставки: {self.calculate_shipping()}")
    
    
class DigitalOrder(Order, Printable, Comparable):
    """Цифровой заказ - реализует интерфейсы Printable и Comparable"""
    
    def __init__(self, name, email, id_order, order_amount, status, pin, download_link, expire_days):
        super().__init__(name, email, id_order, order_amount, status, pin)
        self.download_link = download_link
        self.expire_days = expire_days
        self._created_at = datetime.now()

    def is_valid(self):
        if not self.download_link:
            return False
        
        expire = self._created_at + timedelta(days=self.expire_days)
        return datetime.now() <= expire
    
    def generate_download_link(self):
        self.download_link = f"https://store.com/download/{self.id_order}_{self.name}"
        return self.download_link
    
    def pay_order(self, pin_check):
        result = super().pay_order(pin_check)
        if "успешно оплачен" in result:
            self.generate_download_link()
            return f"{result}\nСсылка для скачивания: {self.download_link}"
        return result
    
    def can_be_returned(self):
        return False
    
    def calculate_total_cost(self):
        return self.amount * 0.85
    
    def get_delivery_deadline(self):
        if self.status == "paid":
            if self.is_valid():
                days_left = (self._created_at + timedelta(days=self.expire_days) - datetime.now()).days
                return f"Ссылка активна еще {days_left} дней"
            else:
                return "Срок действия ссылки истек"
        elif self.status == "new":
            return "После оплаты ссылка будет доступна мгновенно"
        return "Заказ отменен"
    
    def to_string(self):
        """Реализация метода из интерфейса Printable"""
        return (f"Цифровой заказ #{self.id_order} | "
                f"Клиент: {self.name} | "
                f"Сумма: {self.amount} руб | "
                f"Статус: {self.status} | "
                f"Срок действия: {self.expire_days} дней")
    
    def compare_to(self, other):
        """Реализация метода из интерфейса Comparable - сравниваем по сумме со скидкой"""
        if not isinstance(other, Order):
            raise TypeError(f"Невозможно сравнить с типом {type(other)}")
        
        self_cost = self.calculate_total_cost()
        other_cost = other.calculate_total_cost() if hasattr(other, 'calculate_total_cost') else other.amount
        
        if self_cost < other_cost:
            return -1
        elif self_cost > other_cost:
            return 1
        else:
            return 0

    def __str__(self):
        parent_str = super().__str__() 
        return (f"{parent_str}\n"
                f"Ссылка для скачивания: {self.download_link}\n"
                f"Дни действия: {self.expire_days}\n")
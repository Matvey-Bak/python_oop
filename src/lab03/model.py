from lab03.base import Order
from datetime import datetime, timedelta

class PhysicalOrder(Order):
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
    
    def __str__(self):
        parent_str = super().__str__() 
        return (f"{parent_str}\n"
                f"Адрес доставки: {self.delivery_address}\n"
                f"Вес заказа: {self.delivery_weight}\n"
                f"Стоимость доставки: {self.calculate_shipping()}")
    
    
class DigitalOrder(Order):
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


    def __str__(self):
        parent_str = super().__str__() 
        return (f"{parent_str}\n"
                f"Ссылка для скачивания: {self.download_link}\n"
                f"Дни действия: {self.expire_days}\n")


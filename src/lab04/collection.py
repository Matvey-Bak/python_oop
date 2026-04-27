from lab03.model import Order
from lab04.interfaces import Printable, Comparable


class BucketOrder:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Order):
            raise TypeError("Объект не является классом Order")

        for existing_item in self._items:
            if existing_item.id_order == item.id_order:
                return f"Нельзя добавить заказ, который уже есть в корзине"
        
        self._items.append(item)
        return f"Заказ {item.name} успешно добавлен"

    def remove(self, item):
        if item not in self._items:
            print("Данного заказа нет в корзине")
            return
        self._items.remove(item)
        print(f"Заказ {item.name} успешно удален из корзины")

    def get_all(self):
        return self._items.copy()
    
    def find_by_id(self, n_id):
        for item in self._items:
            if item.id_order == n_id:
                return item
        print(f"Заказ с ID:{n_id} не найден")
        return None

    def get_by_type(self, class_type):
        return [item for item in self._items if isinstance(item, class_type)]
    
    def get_printable(self):
        return [item for item in self._items if isinstance(item, Printable)]
    
    def get_comparable(self):
        return [item for item in self._items if isinstance(item, Comparable)]
    

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def remove_at_(self, index):
        if 0 <= index < len(self._items):
            removed_item = self._items.pop(index)
            return removed_item
        else:
            raise IndexError(f"Индекс {index} не входит в диапазон")
        
    def sort_by_amount(self):
        self._items.sort(key=lambda item: item.amount)

    def get_by_amount(self, min_amount, max_amount):
        new_bucket = BucketOrder()
        for order in self._items:
            if min_amount <= order.amount <= max_amount:
                new_bucket.add(order)
        return new_bucket
    
    def __str__(self):
        if not self._items:
            return "Корзина пуста"
        
        result = f"Всего заказов: {len(self._items)}\n"
        result += "\n"
        for i, item in enumerate(self._items, 1):
            result += f"{i}. {item.name}, {item.amount} руб, {item.status}\n"
        return result
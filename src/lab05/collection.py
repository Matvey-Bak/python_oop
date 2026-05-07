from lab01.model import Order
from typing import Any, Callable, List, Optional


class BucketOrder:
    def __init__(self):
        self._items = []

    def add(self, item):
        # if not isinstance(item, Order):
        #     raise TypeError("Объект не является классом Order")

        if item.id_order in self._items:
            return f"Нельзя добавиить заказ котрый уже есть в корзине"
        
        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            print("Данного заказа нет в корзине")
        self._items.remove(item)
        print(f"Заказ {item.name} успешно удален из корзины")

    def get_all(self):
        for item in self._items:
            return self._items.copy()
    
    def find_by_id(self, n_id):
        for item in self._items:
            if item.id_order == n_id:
                return item
        print(f"Заказ с ID:{n_id} не найден")

    def get_by_type(self, class_type):
        return [item for item in self._items if isinstance(item, class_type)]
    
    
    # def get_only_physical(self):
    #     from lab03.models import PhysicalOrder
    #     return self.get_by_type(PhysicalOrder)
    
    # def get_only_digital(self):
    #     from lab03.models import DigitalOrder
    #     return self.get_by_type(DigitalOrder)

    def copy(self) -> 'BucketOrder':
        """
        Создаёт и возвращает копию коллекции.
        
        Returns:
            BucketOrder: Новый объект BucketOrder с копией всех заказов
        """
        new_bucket = BucketOrder()
        new_bucket._items = self._items.copy()  # копируем внутренний список
        return new_bucket
    
    def first(self) -> Optional[Order]:
        """Вернуть первый элемент коллекции"""
        return self._items[0] if self._items else None

    def sort_by(self, key_func: Callable[[Order], Any]) -> 'BucketOrder':
        """
        Сортировка коллекции по функции-стратегии.
        
        Паттерн «Стратегия»: key_func определяет правило сортировки.
        
        Args:
            key_func: Функция, извлекающая значение для сравнения
            
        Returns:
            BucketOrder: Возвращает self для цепочек операций
            
        Example:
            collection.sort_by(by_amount)
            collection.sort_by(lambda o: o.name)
        """
        self._items.sort(key=key_func)
        return self
    
    def filter_by(self, predicate: Callable[[Order], bool]) -> 'BucketOrder':
        """
        Фильтрация коллекции по функции-предикату.
        
        Args:
            predicate: Функция, возвращающая True/False для каждого элемента
            
        Returns:
            BucketOrder: Возвращает self для цепочек операций
            
        Example:
            collection.filter_by(is_expensive)
            collection.filter_by(lambda o: o.amount < 1000)
        """
        self._items = list(filter(predicate, self._items))
        return self
    
    def apply(self, func: Callable[[Order], Any]) -> 'BucketOrder':
        """
        Применить функцию ко всем элементам коллекции.
        
        Функция может быть:
        - Обычной функцией
        - Lambda-выражением
        - Callable-объектом (паттерн «Стратегия»)
        
        Args:
            func: Функция для применения к каждому элементу
            
        Returns:
            BucketOrder: Возвращает self для цепочек операций
            
        Example:
            collection.apply(DiscountStrategy(10))
            collection.apply(lambda o: setattr(o, 'amount', o.amount * 0.9))
        """
        self._items = list(map(func, self._items))
        return self
    
    def map_to(self, transform_func: Callable[[Order], Any]) -> List[Any]:
        """
        Преобразовать коллекцию в новый список (не изменяя оригинал).
        
        Args:
            transform_func: Функция преобразования
            
        Returns:
            List[Any]: Новый список с преобразованными элементами
        """
        return list(map(transform_func, self._items))
    

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
        self._items.sort(key = lambda item: item.amount)

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

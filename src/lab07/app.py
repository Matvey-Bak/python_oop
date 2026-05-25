from typing import List, Optional, Callable, Any
from lab01.model import Order
from lab02.collection import BucketOrder
from lab07.exceptions import OrderNotFoundException, DuplicateOrderException


class OrderApp:
    """Основной класс приложения, управляющий бизнес-логикой."""
    
    def __init__(self, collection: BucketOrder) -> None:
        """
        Инициализация приложения.
        
        Args:
            collection: Коллекция заказов
        """
        self._collection = collection
    
    def add_order(self, name: str, email: str, id_order: int, 
                  order_amount: float, status: str, pin: str) -> None:
        """
        Добавляет новый заказ в коллекцию.
        
        Args:
            name: Имя клиента
            email: Email клиента
            id_order: ID заказа
            order_amount: Сумма заказа
            status: Статус заказа
            pin: Пин-код
            
        Raises:
            DuplicateOrderException: Если заказ с таким ID уже существует
            ValueError: Если данные некорректны
        """

        existing = self._collection.find_by_id(id_order)
        if existing:
            raise DuplicateOrderException(f"Заказ с ID {id_order} уже существует")
        
        order = Order(name, email, id_order, order_amount, status, pin)
        self._collection.add(order)
    
    def remove_order(self, id_order: int, confirm: bool = False) -> None:
        """
        Удаляет заказ из коллекции по ID.
        
        Args:
            id_order: ID заказа для удаления
            confirm: Подтверждение удаления
            
        Raises:
            OrderNotFoundException: Если заказ не найден
        """
        order = self._collection.find_by_id(id_order)
        if order is None:
            raise OrderNotFoundException(f"Заказ с ID {id_order} не найден")
        
        if not confirm:
            raise ValueError("Требуется подтверждение удаления")
        
        self._collection.remove(order)
    
    def find_order_by_id(self, id_order: int) -> Optional[Order]:
        """
        Находит заказ по ID.
        
        Args:
            id_order: ID заказа
            
        Returns:
            Optional[Order]: Найденный заказ или None
        """
        return self._collection.find_by_id(id_order)
    
    def get_all_orders(self) -> List[Order]:
        """
        Возвращает все заказы.
        
        Returns:
            List[Order]: Список всех заказов
        """
        return self._collection.get_all()
    
    def filter_orders_by_amount(self, min_amount: float, max_amount: float) -> BucketOrder:
        """
        Фильтрует заказы по диапазону суммы.
        
        Args:
            min_amount: Минимальная сумма
            max_amount: Максимальная сумма
            
        Returns:
            BucketOrder: Отфильтрованная коллекция
        """
        if min_amount < 0 or max_amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
    
        if min_amount > max_amount:
            raise ValueError("Минимальная сумма не может быть больше максимальной")
    
        return self._collection.get_by_amount(min_amount, max_amount)
    
    def filter_orders_by_status(self, status: str) -> BucketOrder:
        """
        Фильтрует заказы по статусу.
        
        Args:
            status: Статус для фильтрации
            
        Returns:
            BucketOrder: Отфильтрованная коллекция
        """
        filtered = BucketOrder()
        for order in self._collection.get_all():
            if order.status == status:
                filtered.add(order)
        return filtered
    
    def sort_orders(self, strategy: str) -> BucketOrder:
        """
        Сортирует заказы по выбранной стратегии.
        
        Args:
            strategy: Стратегия сортировки ('id', 'name', 'amount', 'status')
            
        Returns:
            BucketOrder: Отсортированная коллекция
        """
        strategies = {
            'id': lambda o: o.id_order,
            'name': lambda o: o.name,
            'amount': lambda o: o.amount,
            'status': lambda o: o.status
        }
        
        if strategy not in strategies:
            raise ValueError(f"Неизвестная стратегия сортировки: {strategy}")
        
        sorted_collection = self._collection.copy()
        sorted_collection.sort_by(strategies[strategy])
        return sorted_collection
    
    def pay_order(self, id_order: int, pin: str) -> str:
        """
        Оплачивает заказ.
        
        Args:
            id_order: ID заказа
            pin: Пин-код для подтверждения
            
        Returns:
            str: Результат операции
        """
        order = self._collection.find_by_id(id_order)
        if order is None:
            raise OrderNotFoundException(f"Заказ с ID {id_order} не найден")
        
        return order.pay_order(pin)
    
    def cancel_order(self, id_order: int) -> str:
        """
        Отменяет заказ.
        
        Args:
            id_order: ID заказа
            
        Returns:
            str: Результат операции
        """
        order = self._collection.find_by_id(id_order)
        if order is None:
            raise OrderNotFoundException(f"Заказ с ID {id_order} не найден")
        
        return order.cancel_order()
    
    def ship_order(self, id_order: int) -> str:
        """
        Отправляет заказ.
        
        Args:
            id_order: ID заказа
            
        Returns:
            str: Результат операции
        """
        order = self._collection.find_by_id(id_order)
        if order is None:
            raise OrderNotFoundException(f"Заказ с ID {id_order} не найден")
        
        return order.ship_order()
    
    def get_statistics(self) -> dict:
        """
        Возвращает статистику по заказам.
        
        Returns:
            dict: Статистика (всего заказов, общая сумма, количество по статусам)
        """
        orders = self._collection.get_all()
        total_amount = sum(o.amount for o in orders)
        status_counts = {}
        
        for status in ['new', 'paid', 'shipped', 'cancelled']:
            status_counts[status] = len([o for o in orders if o.status == status])
        
        return {
            'total_orders': len(orders),
            'total_amount': total_amount,
            'total_earnings': Order.total_earnings,
            'status_counts': status_counts
        }
    
    def get_collection(self) -> BucketOrder:
        """Возвращает коллекцию заказов."""
        return self._collection
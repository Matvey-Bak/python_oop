from typing import Any, Callable


def by_name(order) -> str:
    """
    Стратегия сортировки по имени заказа.
    
    Args:
        order: Объект заказа
        
    Returns:
        str: Имя заказа для сравнения
        
    Example:
        sorted(orders, key=by_name)
    """
    return order.name


def by_amount(order) -> float:
    """
    Стратегия сортировки по сумме заказа.
    
    Args:
        order: Объект заказа
        
    Returns:
        float: Сумма заказа для сравнения
        
    Example:
        sorted(orders, key=by_amount)
    """
    return order._order_amount


def by_status(order) -> str:
    """
    Стратегия сортировки по статусу заказа.
    
    Args:
        order: Объект заказа
        
    Returns:
        str: Статус заказа для сравнения
    """
    return order.status


def by_amount_then_name(order) -> tuple:
    """
    Стратегия сортировки сначала по сумме, затем по имени.
    Использует кортеж для составного ключа.
    
    Args:
        order: Объект заказа
        
    Returns:
        tuple: (сумма, имя) для сравнения
    """
    return (order._order_amount, order.name)


def is_expensive(order, threshold: float = 10000) -> bool:
    """
    Фильтр: отбирает дорогие заказы (сумма > threshold).
    
    Args:
        order: Объект заказа
        threshold: Порог стоимости (по умолчанию 10000)
        
    Returns:
        bool: True если заказ дороже порога
    """
    return order._order_amount > threshold


def is_cheap(order, threshold: float = 5000) -> bool:
    """
    Фильтр: отбирает дешёвые заказы (сумма < threshold).
    
    Args:
        order: Объект заказа
        threshold: Порог стоимости (по умолчанию 5000)
        
    Returns:
        bool: True если заказ дешевле порога
    """
    return order._order_amount < threshold


def is_in_progress(order) -> bool:
    """
    Фильтр: отбирает заказы в обработке.
    
    Args:
        order: Объект заказа
        
    Returns:
        bool: True если статус "в обработке"
    """
    return order.status == "в обработке"


def is_completed(order) -> bool:
    """
    Фильтр: отбирает завершённые заказы.
    
    Args:
        order: Объект заказа
        
    Returns:
        bool: True если статус завершён или доставлен
    """
    return order.status in ["завершён", "доставлен"]



def make_amount_filter(min_amount: float, max_amount: float) -> Callable:
    """
    Фабрика функций: создаёт фильтр по диапазону сумм.
    
    Что такое фабрика функций?
    Это функция, которая создаёт и возвращает другую функцию.
    Внутренняя функция "запоминает" параметры (замыкание).
    
    Args:
        min_amount: Минимальная сумма (включительно)
        max_amount: Максимальная сумма (включительно)
        
    Returns:
        Callable: Функция-фильтр для заказов
        
    Example:
        filter_1000_5000 = make_amount_filter(1000, 5000)
        result = filter_1000_5000(order)
    """
    def amount_filter(order) -> bool:
        return min_amount <= order._order_amount <= max_amount
    return amount_filter


def make_discount_applier(percent: float) -> Callable:
    """
    Фабрика функций: создаёт функцию для применения скидки.
    
    Args:
        percent: Процент скидки (0-100)
        
    Returns:
        Callable: Функция, применяющая скидку к заказу
    """
    def apply_discount(order) -> Any:
        order._order_amount = order._order_amount * (1 - percent / 100)
        return order
    return apply_discount



class DiscountStrategy:
    
    def __init__(self, percent: float):
        """
        Инициализация стратегии скидки.
        
        Args:
            percent: Процент скидки (0-100)
        """
        self.percent = percent
    
    def __call__(self, order) -> Any:
        """
        Вызов объекта как функции.
        Метод __call__ позволяет использовать объект как функцию.
        
        Args:
            order: Объект заказа
            
        Returns:
            Order: Заказ с изменённой суммой
        """
        order._order_amount = order._order_amount * (1 - self.percent / 100)
        return order
    
    def set_percent(self, percent: float):
        """Изменить процент скидки после создания объекта"""
        self.percent = percent


class TaxStrategy:
    """
    Паттерн «Стратегия»: добавление налога к заказу.
    
    Этот класс демонстрирует, как можно легко добавить новую стратегию.
    Коллекция не требует изменений - достаточно передать другой callable-объект.
    """
    
    def __init__(self, percent: float):
        """Инициализация стратегии налога"""
        self.percent = percent
    
    def __call__(self, order) -> Any:
        """Добавить налог к сумме заказа"""
        order._order_amount = order._order_amount * (1 + self.percent / 100)
        return order




class PrintStrategy:
    """
    Паттерн «Стратегия»: форматирование вывода заказа.
    
    Разные стратегии форматирования можно подставлять в коллекцию.
    """
    
    def __init__(self, format_type: str = "simple"):
        """
        Args:
            format_type: Тип форматирования ("simple", "detailed")
        """
        self.format_type = format_type
    
    def __call__(self, order) -> str:
        """Вернуть отформатированную строку"""
        if self.format_type == "simple":
            return f"{order.name}: {order._order_amount} руб."
        elif self.format_type == "detailed":
            return f"Заказ #{order.id_order}: {order.name} | {order._order_amount} руб. | {order.status}"
        return str(order)
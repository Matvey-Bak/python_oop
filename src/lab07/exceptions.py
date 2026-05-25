class OrderNotFoundException(Exception):
    """Исключение: заказ не найден в коллекции."""
    pass


class DuplicateOrderException(Exception):
    """Исключение: заказ с таким ID уже существует."""
    pass


class InvalidOrderDataException(Exception):
    """Исключение: некорректные данные заказа."""
    pass


class OrderOperationException(Exception):
    """Исключение: ошибка при выполнении операции над заказом."""
    pass

ItemNotFoundError = OrderNotFoundException
DuplicateItemError = DuplicateOrderException
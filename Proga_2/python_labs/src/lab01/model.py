class Order:
    def __init__(self, client_name, items_count, order_id, order_status):
        if isinstance(client_name, str) and client_name != "":
            self._client_name = client_name
        if isinstance(items_count, int) and items_count > 0:
            self._items_count = items_count
        if isinstance(order_id, str) and len(order_id) == 6:
            self._order_id = order_id
        if isinstance(order_status, str) and order_status != "":
            self._order_status = order_status
        else:
            return "Введенные данные некорректны"
        
    @property
    def client_name(self):
        return self._client_name
    
    def __str__(self):
        return f"Имя клиента: {self._client_name}, количество заказов {self._items_count}, состояние заказа: {self._order_status}"
    
    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return self._name == other.name and self._order_id == other.order_id
    
    def 


    
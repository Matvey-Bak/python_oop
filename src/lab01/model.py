from validations import (
    _validate_name,
    _validate_email,
    _validate_id_order,
    _validate_order_amount,
    _validate_status,
    _validate_balance,
    _validate_pin
)

class Order:
    total_earnings = 0
    total_orders = 0
    
    def __init__(self, name, email, id_order, order_amount, status, balance, pin):
        result_name = _validate_name(name)
        if result_name is not True:
            raise ValueError(result_name)
        self.name = name

        result_email = _validate_email(email)
        if result_email is not True:
            raise ValueError(result_email)
        self._email = email

        result_id_order = _validate_id_order(id_order)
        if result_id_order is not True:
            raise ValueError(result_id_order)
        self.id_order = id_order

        result_order_amount =  _validate_order_amount(order_amount)
        if result_order_amount is not True:
            raise ValueError(result_order_amount)
        self._order_amount = order_amount

        result_status =  _validate_status(status)
        if result_status is not True:
            raise ValueError(result_status)
        self._status = status

        result_balance =  _validate_balance(balance)
        if result_balance is not True:
            raise ValueError(result_balance)
        self._balance = balance

        result_pin =  _validate_pin(pin)
        if result_pin is not True:
            raise ValueError(result_pin)
        self._pin = pin

        Order.total_orders += 1

    @property
    def get_status(self):
        return self._status
    
    @property
    def get_balance(self):
        return self._balance
    
    @property
    def get_amount(self):
        return self._order_amount
    
    @property
    def gs_email(self): 
        return self._email
    
    @gs_email.setter
    def gs_email(self, new_email):
        if _validate_email(new_email):
            self._email = new_email

    def verify_pin(self, new_pin):
        if _validate_pin(new_pin):
            return self._pin == new_pin

    def can_be_cancelled(self):
        return self._status in ["new", "paid"]
    
    def can_be_paid(self):
        return self._status == "new" and self._balance >= self._order_amount
    
    def can_be_shipped(self):
        return self._status == "paid"
    
    
    def cancel_order(self):
        if not self.can_be_cancelled():
            return f"Заказ со статусом {self._status} нельзя отменить"
        was_paid = (self._status == "paid")
        self._status = "cancelled"
        if was_paid:
            self._balance += self._order_amount
            return f"Заказ успешно отменен деньги возвращены на баланс"
        return f"Заказ успешно отменен"
        
        
    def pay_order(self, pin_check):
        if not _validate_pin(pin_check):
            return f"Ошибка: Пин код не соответствует требованиям"
        if not self.can_be_paid():
            if self._status != "new":
                return f"Нельзя оплатить заказ со статусом {self._status}"
            else:
                return f"Недостаточно средств.(Баланс:{self._balance}), Сумма заказа:{self._order_amount}"
        if not self.verify_pin(pin_check):
            return f"Неверный пин-код"
                           
        self._status = "paid"
        self._balance -= self._order_amount
        Order.total_earnings += self._order_amount
        return f"Заказ успешно оплачен"
    
    def ship_order(self):
        if not self.can_be_shipped():
            return f"Нельзя отправить заказ со статусом {self._status}"
        self._status = "shipped"
        return f"Заказ отправлен"

    

    def __str__(self):
        return (f"Заказ №: {self.id_order}\n"
                f"Клиент: {self.name} \n"
                f"Email клиента: {self._email} \n"
                f"Состояние заказа: {self._status} \n"
                f"Сумма заказа: {self._order_amount}")
    
    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
    
        return self.id_order == other.id_order
    
    def __repr__(self):
        return (f"Order: \n"
                f"id_order = {self.id_order!r} \n"
                f"name = {self.name!r} \n"
                f"email = {self._email!r} \n"
                f"status = {self._status!r} \n"
                f"order_amount = {self._order_amount!r} \n"
        )

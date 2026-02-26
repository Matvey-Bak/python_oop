# Лабораторная работа №1
## Инкапсуляция и класссы в python
### 1. Цели работы:
1. Реализовать класс Order 
2. Создать файл demo для демонстрации работы класса
3. Создать файл validtions где будут храниться все необходимые валидации для класса

## 2. Класс Order 
### 2.1 Конструктор __init__ и атрибуты класса
```python
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
```

### 2.2 Геттеры и сеттеры + методы проверки состояния
``` python
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
```

### 2.3 Бизнес методы
```python
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
```
### 2.4 Магические методы
```python
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
```
## 3. Файл validations
### 3.1 Валидации name, email, id_order, order_amount, status, balance, pin
```python
def _validate_name(obj):
    if not isinstance(obj, str):
        return f"Ошибка: Имя должно быть строкой"
    if not obj.strip():
        return f"Ошибка: Имя не может быть пустым или состоять из пробелов"
    if len(obj) < 6:
        return f"Ошибка: Имя слишком короткое. Минимальная длина: 6 символов "
    if len(obj) > 20:
        return f"Ошибка: Имя слишком длинное. Максимальная длина: 20 символов"

    return True

def _validate_email(obj):
    if not isinstance(obj, str):
        return f"Ошибка: Email должен быть строкой"
    if "@" not in obj or "." not in obj:
        return f"Ошибка: Email должен содержать символы @ и ."
    if len(obj) < 12:
        return f"Ошибка: Длина email слишком короткая. Минимальная длина: 12 символов"
    
    return True

def _validate_id_order(obj):
    if not isinstance(obj, (str, int)):
        return f"Ошибка: ID заказа должно быть числом или строкой"
    
    id_str = str(obj)

    if not id_str:
        return f"ID заказа не может быть пустым"
    if len(id_str) < 5:
        return f"Ошибка: ID заказа слишком короткий. Минимальная длина: 5 символов"
    if len(id_str) > 20:
        return f"Ошибка: ID заказа слишком длинный. Максимальная длина: 20 символов"
    
    return True

def _validate_order_amount(obj):
    if not isinstance(obj, (int, float)):
        return f"Ошибка: Цена заказа должна быть числом"
    if obj <= 0:
        return f"Ошибка: Цена заказа не может быть равна нулю или отрицательному числу"
    
    return True

def _validate_status(obj):
    if not isinstance(obj, str):
        return f"Ошибка: Статус заказа должен быть строкой"
    if obj not in ["new", "paid", "shipped", "cancelled"]:
        return f"Ошибка: Статус заказа не соответствует возможным. Статусы ззаказа: new, paid, shipped, cancelled"
    
    return True

def _validate_balance(obj):
    if not isinstance(obj, (int, float)):
        return f"Ошибка: Баланс должен быть числом"
    if obj < 0:
        return f"Ошибка: Баланс не может быть отрицательным"
    return True
    
def _validate_pin(obj):
    if not isinstance(obj, int):
        return f"Ошибка: Пин код должен быть числом"
    if obj < 0:
        return f"Ошибка: Пин код не может быть отрицательным"
    
    str_pin = str(obj)

    if len(str_pin) < 4:
        return f"Ошибка: Пин код слишком короткий. Минимальная длина пин кода: 4 символа"
    if len(str_pin) > 8:
        return f"Ошибка: Пин код слишком длинный. Максимальная длина пин кода: 8 символов"
    
    return True
    
```

## 4. Demo (Демонстрация)
### 4.1 Конструкция try except
```python
    print("\n Validation")
    try:
        order1 = Order("Tom", "not-email", 123, -100, "invalid", -500, 12)
    except (ValueError, TypeError) as e:
        print("Ошибка благодаря валидации")

```
### 4.2 Создание 2 заказов
```python
order2 = Order("Matvey", "mak@gmail.com",1234567, 5000, "paid", 10000, 1234)
order3 = Order("Nikita", "nik@mail.ru", 7654321, 3000, "new", 5000, 5678)
```

### 4.3 Вывод магических методов
```python
    print(f"\n Вывод __str__")
    print(str(order2))

    print("\n Вывод __repr__")
    print(repr(order2))

    print("\n Вывод __eq__")
    print(order2 == order3)
```

### 4.4 Вывод геттеров и сеттеров
```python
    print("\n Геттеры:")
    print(f"Статус: {order2.get_status}")
    print(f"Баланс: {order2.get_balance}")
    print(f"Стоимость заказа: {order2.get_amount}")
    print(f"Email: {order2.gs_email}")

    print("\n Сеттер:")
    print(f"Старый email {order2.gs_email}")
    order2.gs_email = "makbak@gmail.com"
    print(f"Новый email {order2.gs_email}")
```

### 4.5 Вывод методов состояния
```python
    print("\n Проверка состояния")
    print(f"Можно отменить: {order2.can_be_cancelled()}")
    print(f"Можно оплатить: {order2.can_be_paid()}")
    print(f"Можно отправить: {order2.can_be_shipped()}")
```

### 4.6 Вывод бизнес методов
```python
    print("\n Изменение состояния")
    while True:
        print(20 * "=" + "\n")
        print("Доступные команды:")
        print("1. Отменить заказ")
        print("2. Оплатить заказ")
        print("3. Отправить заказ")
        print("4. Выход" + "\n")
        print(20 * "=")

        command = input("Выберите команду(1-4): ")
        if command == "1":
            print(order2.cancel_order())
        elif command == "2":
            print(order2.pay_order(1234))
        elif command == "3":
            print(order2.ship_order())
        elif command == "4":
            break
        else:
            print(f"Неверная команда")

    if __name__ == "__main__":
        main()



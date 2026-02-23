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
    

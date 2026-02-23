from model import Order

def main():
    print("\n Validation")
    try:
        order1 = Order("Tom", "not-email", 123, -100, "invalid", -500, 12)
    except (ValueError, TypeError) as e:
        print("Ошибка благодаря валидации")

    order2 = Order("Matvey", "mak@gmail.com",1234567, 5000, "paid", 10000, 1234)
    order3 = Order("Nikita", "niktururu@mail.ru", 7654321, 3000, "new", 5000, 5678)

    print(f"\n Вывод __str__")
    print(str(order2))

    print("\n Вывод __repr__")
    print(repr(order2))

    print("\n Вывод __eq__")
    print(order2 == order3)

    print("\n Геттеры:")
    print(f"Статус: {order2.get_status}")
    print(f"Баланс: {order2.get_balance}")
    print(f"Стоимость заказа: {order2.get_amount}")
    print(f"Email: {order2.gs_email}")

    print("\n Сеттер:")
    print(f"Старый email {order2.gs_email}")
    order2.gs_email = "makbak@gmail.com"
    print(f"Новый email {order2.gs_email}")

    print("\n Проверка состояния")
    print(f"Можно отменить: {order2.can_be_cancelled()}")
    print(f"Можно оплатить: {order2.can_be_paid()}")
    print(f"Можно отправить: {order2.can_be_shipped()}")

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
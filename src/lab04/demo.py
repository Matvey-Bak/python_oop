"""
Демонстрация лабораторной работы №5
Тема: Интерфейсы (ABC), полиморфизм, коллекции
"""

from lab04.model import PhysicalOrder, DigitalOrder
from lab04.collection import BucketOrder
from lab04.interfaces import Printable, Comparable


def script1_demonstrate_interfaces():
    """
    Сценарий 1: Демонстрация интерфейсов и полиморфизма
    """
    print("=" * 60)
    print("СЦЕНАРИЙ 1: Демонстрация интерфейсов Printable и Comparable")
    print("=" * 60)
    

    physical1 = PhysicalOrder(
        "Иван Петров", "ivan@mail.ru", 10000001, 1500, "new", 1234,
        "г. Москва, ул. Ленина, д. 10", 25
    )
    
    physical2 = PhysicalOrder(
        "Мария Сидорова", "maria@mail.ru", 11111002, 3000, "paid", 5678,
        "г. СПб, Невский пр., д. 50", 15
    )
    
    digital1 = DigitalOrder(
        "Алексей Иванов", "alex@mail.ru", 224434001, 1000, "new", 4321,
        "", 30
    )
    
    digital2 = DigitalOrder(
        "Елена Смирнова", "elena@mail.ru", 2065565602, 2500, "paid", 8765,
        "https://store.com/download/old", 15
    )
    
    print("1. Оплата заказов:")
    print(digital1.pay_order(4321))
    print(physical2.pay_order(5678))
    print()
    
    print("2. Демонстрация Printable (полиморфный вывод):")
    printables = [physical1, physical2, digital1, digital2]
    for item in printables:
        print(item.to_string())
    print()
    
    print("3. Демонстрация Comparable (сравнение заказов):")
    print(f"Сравнение {physical1.name} ({physical1.amount} руб) и {physical2.name} ({physical2.amount} руб):")
    if physical1.compare_to(physical2) < 0:
        print(f"Результат: {physical1.name} дешевле")
    elif physical1.compare_to(physical2) > 0:
        print(f"Результат: {physical1.name} дороже")
    else:
        print("Результат: суммы равны")
    
    print(f"\nСравнение {digital1.name} ({digital1.calculate_total_cost():.2f} руб со скидкой) "
          f"и {digital2.name} ({digital2.calculate_total_cost():.2f} руб со скидкой):")
    if digital1.compare_to(digital2) < 0:
        print(f"Результат: {digital1.name} дешевле")
    elif digital1.compare_to(digital2) > 0:
        print(f"Результат: {digital1.name} дороже")
    else:
        print("Результат: суммы равны")
    print()


def script2_demonstrate_collection_filtration():
    """
    Сценарий 2: Демонстрация фильтрации коллекции по интерфейсам
    """
    print("=" * 60)
    print("СЦЕНАРИЙ 2: Фильтрация коллекции по интерфейсам")
    print("=" * 60)
    

    physical1 = PhysicalOrder(
        "Иван Петров", "ivan@mail.ru", 105353534501, 1500, "new", 1234,
        "г. Москва, ул. Ленина, д. 10", 25
    )
    
    physical2 = PhysicalOrder(
        "Мария Сидорова", "maria@mail.ru", 10056676662, 3000, "paid", 5678,
        "г. СПб, Невский пр., д. 50", 15
    )
    
    digital1 = DigitalOrder(
        "Алексей Иванов", "alex@mail.ru", 209576766801, 1000, "new", 4321,
        "", 30
    )
    
    digital2 = DigitalOrder(
        "Елена Смирнова", "elena@mail.ru", 2097565602, 2500, "paid", 8765,
        "https://store.com/download/old", 15
    )
    
    bucket = BucketOrder()
    bucket.add(physical1)
    bucket.add(physical2)
    bucket.add(digital1)
    bucket.add(digital2)
    
    print("1. Фильтрация по интерфейсу Printable (get_printable()):")
    printable_orders = bucket.get_printable()
    for item in printable_orders:
        print(f"   {item.to_string()}")
    print(f"   Найдено объектов: {len(printable_orders)}")
    print()
    
    print("2. Фильтрация по интерфейсу Comparable (get_comparable()):")
    comparable_orders = bucket.get_comparable()
    for item in comparable_orders:
        print(f"   {item.to_string()}")
    print(f"   Найдено объектов: {len(comparable_orders)}")
    print()
    
    print("3. Проверка через isinstance():")
    for order in bucket.get_all():
        print(f"   Заказ #{order.id_order} ({order.__class__.__name__}):")
        print(f"      Printable: {isinstance(order, Printable)}")
        print(f"      Comparable: {isinstance(order, Comparable)}")
    print()


def script3_demonstrate_polymorphism():
    """
    Сценарий 3: Демонстрация полиморфизма через интерфейс
    """
    print("=" * 60)
    print("СЦЕНАРИЙ 3: Полиморфизм через интерфейс")
    print("=" * 60)
    
    bucket = BucketOrder()
    

    physical = PhysicalOrder(
        "Иван Петров", "ivan@mail.ru", 18787901, 1500, "paid", 1234,
        "г. Москва, ул. Ленина, д. 10", 25
    )
    
    digital = DigitalOrder(
        "Алексей Иванов", "alex@mail.ru", 20087877971, 1000, "paid", 4321,
        "https://store.com/download/game", 30
    )
    
    bucket.add(physical)
    bucket.add(digital)
    
    physical.pay_order(1234)
    digital.pay_order(4321)
    
    print("1. Полиморфный вызов to_string() для Printable объектов:")
    printable_orders = bucket.get_printable()
    for order in printable_orders:
        print(f"   {order.to_string()}")
    print()
    
    print("2. Универсальная функция через интерфейс:")
    def print_order_details(printable_obj):
        print(f"   {printable_obj.to_string()}")
    
    for order in printable_orders:
        print_order_details(order)
    print()


def main():
    print("\n" + "=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №5")
    print("Интерфейсы (ABC), полиморфизм, коллекции")
    print("=" * 60 + "\n")
    
    script1_demonstrate_interfaces()
    script2_demonstrate_collection_filtration()
    script3_demonstrate_polymorphism()
    
    print("=" * 60)
    print("ИТОГ: Все требования выполнены")
    print("=" * 60)
    print("2 интерфейса (Printable, Comparable)")
    print("2 класса реализуют интерфейсы (PhysicalOrder, DigitalOrder)")
    print("Разная реализация методов в разных классах")
    print("Фильтрация коллекции по интерфейсу")
    print("Полиморфизм через интерфейс")
    print("=" * 60)


if __name__ == "__main__":
    main()
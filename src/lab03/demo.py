
from lab02.collection import BucketOrder
from lab03.model import PhysicalOrder, DigitalOrder


def create_orders_collection():
    bucket = BucketOrder()
    
    bucket.add(PhysicalOrder(
        name="Invinciable",
        email="invincible@globaldefense.com",
        id_order=1015678,
        order_amount=5000,
        status="new",
        pin=1234,
        delivery_address="Chicago",
        delivery_weight=25
    ))
    
    bucket.add(PhysicalOrder(
        name="Omni-Man",
        email="nolan@viltrum.com",
        id_order=1020987,
        order_amount=3500,
        status="paid",
        pin=5678,
        delivery_address="Washington",
        delivery_weight=10
    ))
    
    bucket.add(PhysicalOrder(
        name="Atom Eve",
        email="eve@teen-team.com",
        id_order=1031234,
        order_amount=10000,
        status="cancelled",
        pin=9012,
        delivery_address="Los Angeles",
        delivery_weight=45
    ))
    
    bucket.add(DigitalOrder(
        name="Pudge_arcana",
        email="hook@for_drowka.com",
        id_order=2014567,
        order_amount=3000,
        status="new",
        pin=1111,
        download_link="",
        expire_days=30
    ))
    
    bucket.add(DigitalOrder(
        name="Primal_beast",
        email="pulverize@aghanim_plus_shiva.com",
        id_order=202222,
        order_amount=2500,
        status="paid",
        pin=2222,
        download_link="https://old-link.com",
        expire_days=7
    ))
    
    bucket.add(DigitalOrder(
        name="Drow_Ranger",
        email="Arcana@top1_in_dota2.com",
        id_order=2037656,
        order_amount=4500,
        status="cancelled",
        pin=3333,
        download_link="",
        expire_days=60
    ))
    
    return bucket



def script1(bucket):
    print("\n" + "=" * 70)
    print("СЦЕНАРИЙ 1: Единая коллекция с объектами разных типов")
    print("=" * 70)
    
    print(f"\nВ коллекции {len(bucket)} заказов:")
    print(f"   - Физических заказов: {len(bucket.get_by_type(PhysicalOrder))}")
    print(f"   - Цифровых заказов: {len(bucket.get_by_type(DigitalOrder))}")
    
    print("\n" + "-" * 70)
    print("Содержимое коллекции:")
    print("-" * 70)
    print(bucket)




def script2(bucket):
    print("\n" + "=" * 70)
    print("СЦЕНАРИЙ 2: Полиморфизм — одинаковый метод, разные результаты")
    print("=" * 70)
    print("Вызов calculate_total_cost() и get_delivery_deadline() дает разный результат")
    print("=" * 70)
    
    print("\n" + "-" * 70)
    print("ДЕМОНСТРАЦИЯ: calculate_total_cost()")
    print("-" * 70)
    
    for order in bucket.get_all():
        result = order.calculate_total_cost()
        print(f"\nЗаказ: {order.name}")
        print(f"   Базовая цена: {order.amount}")
        print(f"   Итоговая цена: {result}")
    
    print("\n" + "-" * 70)
    print("ДЕМОНСТРАЦИЯ: get_delivery_deadline()")
    print("-" * 70)
    
    for order in bucket.get_all():
        deadline = order.get_delivery_deadline()
        print(f"\nЗаказ: {order.name}")
        print(f"   Статус: {order.status}")
        print(f"   Срок: {deadline}")


def script3(bucket):
    print("\n" + "=" * 70)
    print("СЦЕНАРИЙ 3: Универсальная фильтрация get_by_type()")
    print("=" * 70)
    print("Один универсальный метод для фильтрации по любому типу")
    print("=" * 70)
    
    print("\n" + "-" * 70)
    print("ПРИМЕР 1: get_by_type(PhysicalOrder) - все физические заказы")
    print("-" * 70)
    physical_orders = bucket.get_by_type(PhysicalOrder)
    print(f"Найдено заказов: {len(physical_orders)}")
    for order in physical_orders:
        print(f"   - {order.name} | тип: Физический | вес: {order.delivery_weight} кг")
    

    print("\n" + "-" * 70)
    print("ПРИМЕР 2: get_by_type(DigitalOrder) - все цифровые заказы")
    print("-" * 70)
    digital_orders = bucket.get_by_type(DigitalOrder)
    print(f"Найдено заказов: {len(digital_orders)}")
    for order in digital_orders:
        print(f"   - {order.name} | тип: Цифровой | дней: {order.expire_days}")


if __name__ == "__main__":    
    bucket = create_orders_collection()
    

    script1(bucket)
    script2(bucket)
    script3(bucket)
    

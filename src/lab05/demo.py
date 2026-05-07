from lab05.collection import BucketOrder, Order
from lab05.strategies import (

    by_name, by_amount, by_amount_then_name,

    is_expensive, is_in_progress,

    make_amount_filter, make_discount_applier,

    DiscountStrategy, TaxStrategy, PrintStrategy
)


def create_test_collection() -> BucketOrder:
    bucket = BucketOrder()
    
    orders = [
        Order(
            name="Baby shark",
            email="akylka@tu.rururru",
            id_order=1769473850786,
            order_amount=4500,
            status="paid",
            pin=1234
        ),

        Order(
            name=" Viper",
            email="poison@attack.ru",
            id_order=32786794736585,
            order_amount=12500,
            status="new",
            pin=5678
        ),
        
        Order(
            name="Gunner",
            email="rockandstone@drg.ru",
            id_order=7755657576963,
            order_amount=3500,
            status="new",
            pin=9012
        ),
        
        Order(
            name="Scoutttt",
            email="deeprock@galactik.ru",
            id_order=4986876889878,
            order_amount=2800,
            status="new",
            pin=3456
        ),
        
        Order(
            name="Driller",
            email="kaboom@c4.com",
            id_order=5086658475,
            order_amount=890,
            status="paid",
            pin=7890
        ),
        
        Order(
            name="Engineer",
            email="autoturret@plazma.com",
            id_order=6788987878,
            order_amount=3200,
            status="paid",
            pin=1111
        ),
        
        Order(
            name="Shadow fiend",
            email="zxcmatusha@requem.ru",
            id_order=79788987907878,
            order_amount=6700,
            status="paid",
            pin=2222
        )
    ]
    
    for order in orders:
        bucket.add(order)
    
    return bucket


def print_separator(title: str):
    """Печать разделителя с заголовком"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def demo_sorting_strategies():
    """СЦЕНАРИЙ 1: Демонстрация разных стратегий сортировки"""
    print_separator("СЦЕНАРИЙ 1: Сортировка разными стратегиями")
    
    bucket = create_test_collection()
    print("\n Исходная коллекция:")
    print(bucket)
    
    print("\n Стратегия 1: Сортировка по имени (by_name)")
    result = bucket.copy().sort_by(by_name)
    print(result)
    
    print("\n Стратегия 2: Сортировка по сумме (by_amount)")
    result = bucket.copy().sort_by(by_amount)
    print(result)

    print("\n Стратегия 3: Сортировка по сумме → по имени (by_amount_then_name)")
    result = bucket.copy().sort_by(by_amount_then_name)
    print(result)


def demo_filtering():
    """СЦЕНАРИЙ 2: Демонстрация фильтрации"""
    print_separator("СЦЕНАРИЙ 2: Фильтрация коллекции")
    
    bucket = create_test_collection()
    print("\n Исходная коллекция:")
    print(bucket)
    
    print("\n Фильтр 1: Дорогие заказы (> 10000 руб.)")
    result = bucket.copy().filter_by(is_expensive)
    print(result if len(result) > 0 else "  (пусто)")
    
    print("\n Фильтр 2: Заказы в обработке")
    result = bucket.copy().filter_by(is_in_progress)
    print(result)
    
    print("\n Фильтр 3: Заказы от 5000 до 15000 руб. (lambda)")
    result = bucket.copy().filter_by(lambda o: 5000 <= o.amount <= 15000)
    print(result)


def demo_map_and_factories():
    """СЦЕНАРИЙ 3: map() и фабрики функций"""
    print_separator("СЦЕНАРИЙ 3: map() и фабрики функций")
    
    bucket = create_test_collection()
    
    print("\n map() - извлечение имён заказов:")
    names = bucket.map_to(lambda o: o.name)
    print(f"   {names}")
    
    print("\n map() - извлечение сумм заказов:")
    amounts = bucket.map_to(lambda o: o.amount)
    print(f"   {amounts}")
    

    print("\n Фабрика функций: make_amount_filter(5000, 50000)")
    print("   Создаём фильтр заказов от 5000 до 50000 руб.")
    
    filter_range = make_amount_filter(5000, 50000)
    filtered = bucket.copy().filter_by(filter_range)
    print(f"\n   Результат:")
    print(filtered)
    
    print("\n Фабрика функций: make_discount_applier(10%)")
    apply_10_discount = make_discount_applier(10)
    
    test_bucket = bucket.copy()
    print("   До применения скидки (первые 3 заказа):")
    for order in test_bucket.get_all()[:3]:
        print(f"     {order.name}: {order.amount} руб.")
    
    test_bucket.apply(apply_10_discount)
    print("\n   После скидки 10% (первые 3 заказа):")
    for order in test_bucket.get_all()[:3]:
        print(f"     {order.name}: {order.amount:.2f} руб.")


def demo_chain_operations():
    """СЦЕНАРИЙ 4: Цепочка операций (filter → sort → apply)"""
    print_separator("СЦЕНАРИЙ 4: Цепочка операций filter → sort → apply")
    
    bucket = create_test_collection()
    print("\n Исходная коллекция:")
    print(bucket)
    
    print("\n Цепочка операций:")
    print("   1. filter_by(заказы в обработке)")
    print("   2. sort_by(по сумме, от дешёвых к дорогим)")
    print("   3. apply(скидка 10% на все отфильтрованные заказы)")
    
    result = (bucket.copy()
        .filter_by(lambda o: o.status == "в обработке")
        .sort_by(by_amount)
        .apply(DiscountStrategy(10)))
    
    print("\n Результат цепочки:")
    print(result)
    
    print("\n Обратите внимание: методы возвращают self,")
    print("   поэтому их можно выстраивать в цепочку.")


def demo_callable_strategies():
    """СЦЕНАРИЙ 5: Callable-объекты (паттерн Стратегия)"""
    print_separator("СЦЕНАРИЙ 5: Callable-объекты (паттерн «Стратегия»)")
    
    bucket = create_test_collection()
    
    print("\n DiscountStrategy (скидка 15%):")
    discount_15 = DiscountStrategy(15)
    
    test_order = Order(
            name="Baby shark",
            email="akylka@tu.rururru",
            id_order=1769473850786,
            order_amount=4500,
            status="paid",
            pin=1234
        )
    print(f"   До скидки: {test_order.amount} руб.")
    discount_15(test_order) 
    print(f"   После скидки 15%: {test_order.amount} руб.")
    
  
    print("\n TaxStrategy (налог 20%):")
    tax_20 = TaxStrategy(20)
    
    test_order2 = Order("Lose_my_mind", "Dojacat_from_F1@leclerc.com", 755565657575, 5000, "new", 1234)
    print(f"   До налога: {test_order2.amount} руб.")
    tax_20(test_order2)
    print(f"   После налога 20%: {test_order2.amount} руб.")
    
    
    print("\n PrintStrategy (разные форматы вывода):")
    simple_printer = PrintStrategy("simple")
    detailed_printer = PrintStrategy("detailed")
    
    order = bucket.first()
    if order:
        print(f"   Simple: {simple_printer(order)}")
        print(f"   Detailed: {detailed_printer(order)}")
    



def main():
    """Главная функция - запуск всех сценариев"""
    print("\n" + "=" * 55)
    print("     ЛАБОРАТОРНАЯ РАБОТА №5 - ВАРИАНТ НА 5")
    print("     Функции как аргументы. Стратегии и делегаты.")
    print("     Паттерн «Стратегия» через callable-объекты")
    print("=" * 55)
    
    demo_sorting_strategies()
    demo_filtering()
    demo_map_and_factories()
    demo_chain_operations()
    demo_callable_strategies()
    

if __name__ == "__main__":
    main()
from lab06.container import DisplayableCollection, ScorableCollection, Displayable, Scorable
from lab03.model import PhysicalOrder, DigitalOrder


print("="*60)
print("СЦЕНАРИЙ 1: TypedCollection[D] - объекты с методом display()")
print("="*60)

displayable_items = DisplayableCollection()

physical = PhysicalOrder(
    name="Иван Петров",
    email="ivan@mail.ru", 
    id_order=1767684943394,
    order_amount=1500.0,
    status="new",
    pin=1234,
    delivery_address="ул. Ленина, 10",
    delivery_weight=2.5
)

digital = DigitalOrder(
    name="Мария Сидорова",
    email="maria@mail.ru",
    id_order=234567890543,
    order_amount=500.0,
    status="paid",
    pin=5678,
    download_link="https://download.com/order2",
    expire_days=30
)

displayable_items.add(physical)
displayable_items.add(digital)

print("\nДобавлены объекты из иерархии ЛР-3 (без наследования от Protocol):")
print(f"  • PhysicalOrder - имеет display()? {hasattr(physical, 'display')}")
print(f"  • DigitalOrder - имеет display()? {hasattr(digital, 'display')}")



print("\n--- Вызов display() для каждого объекта ---")
for item in displayable_items.get_all():
    print(f"  {item.display()}")


print("\n--- Использование map() с display() (меняем тип T → str) ---")
displays = displayable_items.map(lambda x: x.display())
print(f"  Тип результата: {type(displays)}")
print(f"  Тип элементов: {type(displays[0])} (str)")
for i, text in enumerate(displays, 1):
    print(f"  {i}. {text[:60]}...")


print("\n" + "="*60)
print("СЦЕНАРИЙ 2: TypedCollection[S] - объекты с методом score()")
print("="*60)

scorable_items = ScorableCollection()

physical2 = PhysicalOrder(
    name="Алексей Иванов",
    email="alex@mail.ru",
    id_order=3659374977654739,
    order_amount=2000.0,
    status="new",
    pin=9012,
    delivery_address="ул. Пушкина, 5",
    delivery_weight=3.0
)

digital2 = DigitalOrder(
    name="Елена Смирнова",
    email="elena@mail.ru",
    id_order=44429402374,
    order_amount=750.0,
    status="new",
    pin=3456,
    download_link="https://download.com/order4",
    expire_days=15
)

scorable_items.add(physical2)
scorable_items.add(digital2)

print("\nДобавлены объекты из иерархии ЛР-3 (без наследования от Protocol):")
print(f"  • PhysicalOrder - имеет score()? {hasattr(physical2, 'score')}")
print(f"  • DigitalOrder - имеет score()? {hasattr(digital2, 'score')}")



print("\n--- Значения score() для каждого объекта ---")
for item in scorable_items.get_all():
    if isinstance(item, PhysicalOrder):
        formula = "delivery_weight*10 + amount/100"
        score_value = item.weight * 10 + item.amount / 100
    else:  
        formula = "amount/50"
        score_value = item.amount / 50
    print(f"  {item.__class__.__name__}: score = {item.score():.2f}")
    print(f"    (формула: {formula})")
    print(f"    Проверка: {score_value:.2f} = {item.score():.2f}")

print("\n--- Статистика коллекции ---")
print(f"  Общая сумма score: {scorable_items.get_total_score():.2f}")
print(f"  Среднее значение score: {scorable_items.get_average_score():.2f}")

print("\n--- Использование map() с score() (меняем тип T → float) ---")
scores = scorable_items.map(lambda x: x.score())
print(f"  Тип результата: {type(scores)}")
print(f"  Тип элементов: {type(scores[0])} (float)")
print(f"  Список score: {scores}")


print("\n" + "="*60)
print("Демонстрация find() и filter()")
print("="*60)

print("\n--- find() - поиск заказа с весом > 2.7 ---")
found = scorable_items.find(lambda x: isinstance(x, PhysicalOrder) and x.weight > 2.7)
if found:
    print(f"  ✓ Найден: {found.display()}")
    print(f"    Вес: {found.weight} кг")

print("\n--- find() - поиск заказа с весом > 10 ---")
not_found = scorable_items.find(lambda x: isinstance(x, PhysicalOrder) and x.weight > 10)
if not_found is None:
    print(f"  ✓ Элемент не найден (вернулся None)")

print("\n--- filter() - цифровые заказы ---")
digital_orders = scorable_items.filter(lambda x: isinstance(x, DigitalOrder))
print(f"  Найдено {len(digital_orders)} цифровых заказов:")
for order in digital_orders:
    print(f"    • {order.display()}")

print("\n--- filter() - заказы с score > 100 ---")
high_score_orders = scorable_items.filter(lambda x: x.score() > 100)
print(f"  Найдено {len(high_score_orders)} заказов:")
for order in high_score_orders:
    print(f"    • {order.display()} (score: {order.score():.2f})")


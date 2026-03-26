from lab01.model import Order
from lab02.model import BucketOrder

class Cat:
    def __init__(self, name, mail, id, amount, stat, pin):
        self.name = name


order1 = Order("Car_Audi", "hghgghgh@fhfhfh.ru", 123456789, 200, "new", 1234)
#order2 = Cat("Ship_Any", "robot@jfjfjfj.com", 987654321, 300, "paid", 9876)
order3 = Order("Plane_Emirates", "plane@vzhuh.com", 456123789, 300, "new", 4567)
order4 = Order("Mountain_Bike", "cycle@trrrrrrr.com", 789123456, 50, "paid", 1928)
order5 = Order("Mountain_cycle", "cycle@trrrrrrr.com", 789123456, 500, "new", 1928)


bucket = BucketOrder()


bucket.add(order1)
bucket.add(order3)
bucket.add(order4)


# print("1. Выводим заказ по индексу \n ")
# print(bucket[0])

# print("\n 2. демонстрация сортировки по цене ")
# print("До сортировки:")
# print(bucket)
# print("После сортировки")
# bucket.sort_by_amount()
# print(bucket)
# print("\n 3. Демонстрация фильтрации")
# print(" bucket до фильтрации" + "\n")
# print(bucket)
# print("bucket после фильтрации" + "\n")
# new_bucket = bucket.get_by_amount(100, 600)
# print(new_bucket)

# print("\n Первый сценарий: Добавляем заказы, ищем какойто заказ, удаляем какой то заказ")
# bucket1 = BucketOrder()
# order1 = Order("Car_Audi", "hghgghgh@fhfhfh.ru", 123456789, 200, "new", 1234)
# #order2 = Cat("Ship_Any", "robot@jfjfjfj.com", 987654321, 300, "paid", 9876)
# order2 = Order("Plane_Emirates", "plane@vzhuh.com", 456123789, 300, "new", 4567)
# order3 = Order("Mountain_Bike", "cycle@trrrrrrr.com", 789123456, 50, "paid", 1928)

# print("\n 1. добавляем заказы в bucket")
# bucket1.add(order1)
# bucket1.add(order2)
# bucket1.add(order3)
# print(bucket1)
# print("\n 2. Ищем элемент по ID")
# print(bucket1.find_by_id(123456789))
# print("\n 3. Удаляем элемент")
# print("Bucket1 до удаления order2")
# print(bucket1)
# bucket1.remove(order2)
# print("\n Bucket1 после удаления")
# print(bucket1)

# print("\n Второй сценарий: Удаляем элемент по индексу")
# print("\n 1. Удаляем элемент по индексу 0")
# print("Корзина до удаления")
# print(bucket1)
# print("Корзина после удаления")
# bucket1.remove_at_index(0)
# print(bucket1)

# print("\n Третий сценарий: сортируем по цене, создаем новую корзину с заказами заданной суммы")
# print("\n 1. Сортируем по цене")
# print("Корзина до сортировки")
# bucket1.add(order1)
# print(bucket1)
# print("\n Корзина после сортировки")
# bucket1.sort_by_amount()
# print(bucket1)
# print("\n 2. Добавляем заказы в промежутке 100 - 600 в новую корзину")
# print(bucket1.get_by_amount(100, 600))


print("Dunder methods: ")
print("__len__")
print(len(bucket))
print("\n __getitem__")
print(bucket[0])
print("\n __str__")
print(bucket)

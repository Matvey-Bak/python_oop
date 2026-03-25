from lab01.model import Order
from lab02.model import BucketOrder

class Cat:
    def __init__(self, name, mail, id, amount, stat, pin):
        self.name = name


order1 = Order("Car_Audi", "hghgghgh@fhfhfh.ru", 123456789, 200, "new", 1234)
#order2 = Cat("Ship_Any", "robot@jfjfjfj.com", 987654321, 300, "paid", 9876)
order3 = Order("Plane_Emirates", "plane@vzhuh.com", 456123789, 300, "new", 4567)
order4 = Order("Mountain_Bike", "cycle@trrrrrrr.com", 789123456, 50, "paid", 1928)
order5 = Order("Mountain", "cycle@trrrrrrr.com", 789123456, 500, "new", 1928)


bucket = BucketOrder()


bucket.add(order1)
bucket.add(order3)
bucket.add(order4)


print("1. Выводим заказ по индексу \n ")
print(bucket[0])

print("\n 2. демонстрация сортировки по цене ")
print("До сортировки:")
print(bucket)
print("После сортировки")
bucket.sort_by_amount()
print(bucket)
print("\n 3. Демонстрация фильтрации")
print(" bucket до фильтрации" + "\n")
print(bucket)
print("bucket после фильтрации" + "\n")
new_bucket = bucket.get_by_amount(100, 600)
print(new_bucket)


    




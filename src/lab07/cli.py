from typing import List, Optional
from lab01.model import Order
from lab02.collection import BucketOrder
from lab07.app import OrderApp
from lab07.exceptions import OrderNotFoundException, DuplicateOrderException


class OrderCLI:
    """Класс для управления консольным интерфейсом."""
    
    def __init__(self, app: OrderApp) -> None:
        """
        Инициализация CLI.
        
        Args:
            app: Экземпляр приложения с бизнес-логикой
        """
        self._app = app
    
    def display_menu(self) -> None:
        """Отображает главное меню."""
        print("\n" + "=" * 50)
        print("          ИНТЕРНЕТ-МАГАЗИН - УПРАВЛЕНИЕ ЗАКАЗАМИ")
        print("=" * 50)
        print("1. Добавить заказ")
        print("2. Показать все заказы")
        print("3. Найти заказ по ID")
        print("4. Удалить заказ")
        print("5. Фильтрация заказов")
        print("6. Сортировка заказов")
        print("7. Операции с заказом (оплата/отмена/отправка)")
        print("8. Статистика")
        print("0. Выход")
        print("-" * 50)
    
    def get_user_choice(self) -> int:
        """
        Получает выбор пользователя из меню.
        
        Returns:
            int: Выбранный пункт меню
        """
        while True:
            try:
                choice = input("Выберите пункт меню: ")
                return int(choice)
            except ValueError:
                self.display_error("Пожалуйста, введите число")
    
    def get_input(self, prompt: str, validator: Optional[callable] = None) -> str:
        """
        Получает ввод пользователя с валидацией.
        
        Args:
            prompt: Приглашение для ввода
            validator: Функция-валидатор
            
        Returns:
            str: Введенное значение
        """
        while True:
            value = input(prompt)
            if validator is None or validator(value):
                return value
            self.display_error("Некорректный ввод. Попробуйте снова.")
    
    def display_error(self, message: str) -> None:
        """Отображает сообщение об ошибке."""
        print(f"\n ОШИБКА: {message}\n")
    
    def display_success(self, message: str) -> None:
        """Отображает сообщение об успехе."""
        print(f"\n {message}\n")
    
    def display_orders_table(self, orders: List[Order]) -> None:
        """
        Отображает заказы в виде таблицы.
        
        Args:
            orders: Список заказов для отображения
        """
        if not orders:
            print("\n Заказов не найдено.\n")
            return
        
        print("\n" + "=" * 80)
        print(f"{'ID':<6} {'Клиент':<20} {'Сумма':<10} {'Статус':<12} {'Email'}")
        print("-" * 80)
        
        for order in orders:
            print(f"{order.id_order:<6} {order.name:<20} {order.amount:<10.2f} {order.status:<12} {order.email}")
        
        print("=" * 80)
        print(f"Всего заказов: {len(orders)}\n")
    
    def display_order_details(self, order: Order) -> None:
        """
        Отображает детальную информацию о заказе.
        
        Args:
            order: Заказ для отображения
        """
        print("\n" + "=" * 50)
        print("ДЕТАЛИ ЗАКАЗА")
        print("=" * 50)
        print(order)
        print("=" * 50 + "\n")
    
    def confirm_action(self, action: str) -> bool:
        """
        Запрашивает подтверждение опасного действия.
        
        Args:
            action: Описание действия
            
        Returns:
            bool: True если подтверждено, False иначе
        """
        response = input(f"\n  {action}? (y/n): ").lower()
        return response == 'y'
    
    def add_order_flow(self) -> None:
        """Поток добавления нового заказа."""
        print("\n--- ДОБАВЛЕНИЕ НОВОГО ЗАКАЗА ---")
        
        try:
            name = self.get_input("Имя клиента: ")
            email = self.get_input("Email клиента: ")
            
            while True:
                try:
                    id_order = int(self.get_input("ID заказа (число): "))
                    break
                except ValueError:
                    self.display_error("ID должен быть числом")
            
            while True:
                try:
                    order_amount = float(self.get_input("Сумма заказа: "))
                    if order_amount > 0:
                        break
                    self.display_error("Сумма должна быть положительной")
                except ValueError:
                    self.display_error("Введите число")
            
            print("Доступные статусы: new, paid, shipped, cancelled")
            status = self.get_input("Статус заказа: ")
            
            pin_input = self.get_input("Пин-код (4-6 цифр): ")
            pin = int(pin_input)
            
            self._app.add_order(name, email, id_order, order_amount, status, pin)
            self.display_success(f"Заказ #{id_order} успешно добавлен!")
            
        except DuplicateOrderException as e:
            self.display_error(str(e))
        except ValueError as e:
            self.display_error(f"Ошибка валидации: {e}")
        except Exception as e:
            self.display_error(f"Неожиданная ошибка: {e}")
    
    def show_all_orders_flow(self) -> None:
        """Поток отображения всех заказов."""
        orders = self._app.get_all_orders()
        self.display_orders_table(orders)
    
    def find_order_flow(self) -> None:
        """Поток поиска заказа по ID."""
        print("\n--- ПОИСК ЗАКАЗА ---")
        
        try:
            id_order = int(self.get_input("Введите ID заказа: "))
            order = self._app.find_order_by_id(id_order)
            
            if order:
                self.display_order_details(order)
            else:
                self.display_error(f"Заказ с ID {id_order} не найден")
                
        except ValueError:
            self.display_error("ID должен быть числом")
    
    def remove_order_flow(self) -> None:
        """Поток удаления заказа."""
        print("\n--- УДАЛЕНИЕ ЗАКАЗА ---")
        
        try:
            id_order = int(self.get_input("Введите ID заказа для удаления: "))
            order = self._app.find_order_by_id(id_order)
            
            if not order:
                self.display_error(f"Заказ с ID {id_order} не найден")
                return
            
            self.display_order_details(order)
            
            if self.confirm_action(f"Удалить заказ #{id_order}"):
                self._app.remove_order(id_order, confirm=True)
                self.display_success(f"Заказ #{id_order} успешно удален!")
            else:
                self.display_success("Удаление отменено")
                
        except ValueError:
            self.display_error("ID должен быть числом")
        except OrderNotFoundException as e:
            self.display_error(str(e))
    
    def filter_orders_flow(self) -> None:
        """Поток фильтрации заказов."""
        print("\n--- ФИЛЬТРАЦИЯ ЗАКАЗОВ ---")
        print("1. Фильтр по диапазону суммы")
        print("2. Фильтр по статусу")
        
        try:
            choice = int(self.get_input("Выберите тип фильтрации: "))
            
            if choice == 1:
                try:
                    min_amount = float(self.get_input("Минимальная сумма: "))
                    max_amount = float(self.get_input("Максимальная сумма: "))
                    filtered = self._app.filter_orders_by_amount(min_amount, max_amount)
                    self.display_orders_table(filtered.get_all())
                except ValueError:
                    self.display_error("Введите корректные числа")
                    
            elif choice == 2:
                print("Доступные статусы: new, paid, shipped, cancelled")
                status = self.get_input("Статус для фильтрации: ")
                filtered = self._app.filter_orders_by_status(status)
                self.display_orders_table(filtered.get_all())
            else:
                self.display_error("Неверный выбор")
                
        except ValueError:
            self.display_error("Введите число")
    
    def sort_orders_flow(self) -> None:
        """Поток сортировки заказов."""
        print("\n--- СОРТИРОВКА ЗАКАЗОВ ---")
        print("1. По ID")
        print("2. По имени клиента")
        print("3. По сумме заказа")
        print("4. По статусу")
        
        strategy_map = {
            '1': 'id',
            '2': 'name',
            '3': 'amount',
            '4': 'status'
        }
        
        choice = self.get_input("Выберите стратегию сортировки: ")
        
        if choice in strategy_map:
            sorted_collection = self._app.sort_orders(strategy_map[choice])
            self.display_orders_table(sorted_collection.get_all())
        else:
            self.display_error("Неверный выбор стратегии")
    
    def order_operations_flow(self) -> None:
        """Поток операций над заказом (оплата/отмена/отправка)."""
        print("\n--- ОПЕРАЦИИ С ЗАКАЗОМ ---")
        print("1. Оплатить заказ")
        print("2. Отменить заказ")
        print("3. Отправить заказ")
        
        try:
            choice = int(self.get_input("Выберите операцию: "))
            id_order = int(self.get_input("Введите ID заказа: "))
            
            if choice == 1:
                pin = self.get_input("Введите пин-код: ")
                result = self._app.pay_order(id_order, pin)
                self.display_success(result)
            elif choice == 2:
                result = self._app.cancel_order(id_order)
                self.display_success(result)
            elif choice == 3:
                result = self._app.ship_order(id_order)
                self.display_success(result)
            else:
                self.display_error("Неверный выбор")
                
        except ValueError:
            self.display_error("Введите корректные данные")
        except OrderNotFoundException as e:
            self.display_error(str(e))
    
    def show_statistics_flow(self) -> None:
        """Поток отображения статистики."""
        stats = self._app.get_statistics()
        
        print("\n" + "=" * 50)
        print("СТАТИСТИКА ЗАКАЗОВ")
        print("=" * 50)
        print(f" Всего заказов: {stats['total_orders']}")
        print(f" Общая сумма заказов: {stats['total_amount']:.2f} руб")
        print(f" Общая выручка: {stats['total_earnings']:.2f} руб")
        print("\n Распределение по статусам:")
        print(f"   • Новые: {stats['status_counts']['new']}")
        print(f"   • Оплаченные: {stats['status_counts']['paid']}")
        print(f"   • Отправленные: {stats['status_counts']['shipped']}")
        print(f"   • Отмененные: {stats['status_counts']['cancelled']}")
        print("=" * 50 + "\n")
    
    def run(self) -> None:
        """Главный цикл приложения."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == 1:
                self.add_order_flow()
            elif choice == 2:
                self.show_all_orders_flow()
            elif choice == 3:
                self.find_order_flow()
            elif choice == 4:
                self.remove_order_flow()
            elif choice == 5:
                self.filter_orders_flow()
            elif choice == 6:
                self.sort_orders_flow()
            elif choice == 7:
                self.order_operations_flow()
            elif choice == 8:
                self.show_statistics_flow()
            elif choice == 0:
                if self.confirm_action("Выйти из программы"):
                    self.display_success("До свидания!")
                    break
            else:
                self.display_error("Неверный пункт меню. Попробуйте снова.")
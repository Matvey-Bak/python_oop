import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab02.collection import BucketOrder
from lab07.app import OrderApp
from lab07.cli import OrderCLI
from lab07.storage import load, save


def main() -> None:
    """
    Главная функция приложения.
    Загружает данные, создает экземпляры классов и запускает CLI.
    """

    data_file = os.path.join(os.path.dirname(__file__), 'orders_data.json')
    
    print("=" * 50)
    print("   ЗАГРУЗКА ДАННЫХ...")
    print("=" * 50)
    
    collection = load(data_file)
    
    app = OrderApp(collection)
    cli = OrderCLI(app)
    
    print(f" Загружено заказов: {len(collection.get_all())}")
    
    cli.run()
    
    print("\n" + "=" * 50)
    print("   СОХРАНЕНИЕ ДАННЫХ...")
    print("=" * 50)
    save(app.get_collection(), data_file)
    print(f" Сохранено заказов: {len(app.get_all_orders())}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Программа прервана пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"\n Критическая ошибка: {e}")
        sys.exit(1)
import json
import os
from typing import List
from lab01.model import Order
from lab02.collection import BucketOrder


def save(collection: BucketOrder, filepath: str) -> None:
    """
    Сохраняет коллекцию заказов в JSON-файл.
    
    Args:
        collection: Объект BucketOrder для сохранения
        filepath: Путь к файлу для сохранения
    """
    data = []
    for order in collection.get_all():
        data.append(order.to_dict())
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load(filepath: str) -> BucketOrder:
    """
    Загружает коллекцию заказов из JSON-файла.
    
    Args:
        filepath: Путь к файлу для загрузки
        
    Returns:
        BucketOrder: Загруженная коллекция заказов
    """
    collection = BucketOrder()
    
    if not os.path.exists(filepath):
        return collection
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for order_data in data:
            try:
                order = Order.from_dict(order_data)
                collection.add(order)
            except (ValueError, KeyError) as e:
                print(f"Ошибка загрузки заказа: {e}")
                
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Ошибка при загрузке файла: {e}")
    
    return collection
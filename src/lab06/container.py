from typing import TypeVar, Generic, Callable, Optional, Protocol, List
from lab01.model import Order

T = TypeVar('T')
R = TypeVar('R')

class Displayable(Protocol):
    def display(self) -> str:
        ...

class Scorable(Protocol):
    def score(self) -> float:
        ...

D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)


class TypedCollection(Generic[T]):
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        if item not in self._items:
            print(f"Элемент не найден в коллекции")
            return
        self._items.remove(item)
        print(f"Элемент успешно удален из коллекции")
    
    def get_all(self) -> List[T]:
        return list(self._items)
    
    def find_by_id(self, n_id: int) -> Optional[T]:
        for item in self._items:
            if hasattr(item, 'id_order') and item.id_order == n_id:
                return item
        print(f"Элемент с ID:{n_id} не найден")
        return None
    
    def get_by_type(self, class_type: type) -> List[T]:
        return [item for item in self._items if isinstance(item, class_type)]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        return self._items[index]
    
    def remove_at(self, index: int) -> Optional[T]:
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        else:
            raise IndexError(f"Индекс {index} не входит в диапазон")
    
    def sort_by_amount(self) -> None:
        self._items.sort(key=lambda item: getattr(item, 'amount', 0))
    
    def get_by_amount(self, min_amount: float, max_amount: float) -> 'TypedCollection[T]':
        new_collection = TypedCollection[T]()
        for item in self._items:
            amount = getattr(item, 'amount', 0)
            if min_amount <= amount <= max_amount:
                new_collection.add(item)
        return new_collection
    
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]
    
    def __str__(self) -> str:
        if not self._items:
            return "Коллекция пуста"
        
        result = f"Всего элементов: {len(self._items)}\n"
        result += "-" * 30 + "\n"
        for i, item in enumerate(self._items, 1):
            result += f"{i}. {str(item)}\n"
        return result


class DisplayableCollection(TypedCollection[D]):
    def display_all(self) -> None:
        for item in self._items:
            print(item.display())


class ScorableCollection(TypedCollection[S]):
    def get_total_score(self) -> float:
        return sum(item.score() for item in self._items)
    
    def get_average_score(self) -> float:
        if not self._items:
            return 0.0
        return self.get_total_score() / len(self._items)
from abc import ABC, abstractmethod

class Printable(ABC):
    
    @abstractmethod
    def to_string(self) -> str:
        pass


class Comparable(ABC):
    
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнивает текущий объект с другим
        Возвращает:
        * отрицательное число, если self < other
        * 0, если self == other
        * положительное число, если self > other
        """
        pass
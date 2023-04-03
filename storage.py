from abc import ABC, abstractmethod

class Storage(ABC):

    def __init__(self, items: dict[str, int], capacity: int):
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, title: str, amount: int) -> None:
        pass

    @abstractmethod
    def remove(self, title: str, amount: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass

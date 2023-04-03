from storage import Storage


class Store(Storage):
    def __init__(self, items: dict[str, int], capacity: int = 100):
        super().__init__(items, capacity)

    def add(self, title: str, amount: int) -> None:
        if amount <= self.capacity:
            self.items[title] = self.items.get(title, 0)
            self.items[title] += amount
            self.capacity -= amount
        else:
            print('На складе недотаточно места. Попробуйте еще раз')

    def remove(self, title: str, amount: int) -> None:
        if title not in self.items.keys():
            print("Такого товара нет на складе")
            return
        elif 0 < amount <= self.items[title]:
            self.items[title] -= amount
            self.capacity += amount
        else:
            print(f"Товара на складе {sum(self.items.values())}. Вы ничего не можете забрать.")
        if self.items[title] == 0:
            self.items.pop(title)

    def get_free_space(self) -> int:
        return self.capacity - sum(self.items.values())

    def get_items(self) -> dict[str, int]:
        return self.items

    def get_unique_items_count(self) -> int:
        return len(self.items.keys())

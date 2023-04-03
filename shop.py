from store import Store


class Shop(Store):
    def __init__(self, items: dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, title: str, amount: int) -> None:
        keys = self.items.keys()
        if title not in keys and len(keys) == 5:
            print("Ошибка. В магазине не может храниться больше 5 товаров")
        if amount <= self.capacity:
            self.items[title] = self.items.get(title, 0)
            self.items[title] += amount
            self.capacity -= amount
        else:
            print('На складе недотаточно места. Попробуйте еще раз')
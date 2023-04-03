from shop import Shop
from store import Store
from request import Request


def main():
    store = Store({
        "миндаль": 16,
        "шоколадки": 23,
        "велосипеды": 7
    })
    shop = Shop({
        "шоколадки": 6,
        "велосипеды": 2,
        "торты": 1
    })

    print('Добрый день! Приветствуем Вас в сети магазинов "Amarrok"\n'
          'Для дальнейших действий, нужно написать запрос, следуя инструкции:\n'
          '1) Для выгрузки из склада в магазин:\n'
          '"Доставить (кол-во) (товар) из склада в магазин".\n'
          '2) Для возвращения товара из магазина в склад:\n'
          '"Вернуть (кол-во) (товар) из магазина в склад".\n'
          'Сейчас на складе:\n'
          f'{store.get_items()}\n'
          'Сейчас в магазине:\n'
          f'{shop.get_items()}\n'
          'Для завершения программы, введите "Завершить".\n'
          'Пора писать запрос!')
    while True:
        req = input().lower()
        if req == "завершить":
            print("Пока-пока")
            break
        try:
            request = Request(req)
        except ValueError:
            print("Неверный запрос, попробуйте ещё раз.")
            continue
        if request.to == 'магазин':
            shop.add(request.product, request.amount)
            store.remove(request.product, request.amount)
        elif request.to == 'склад':
            store.add(request.product, request.amount)
            shop.remove(request.product, request.amount)

        print('Сейчас на складе:'
          f'{store.get_items()}'
          'Сейчас в магазине:'
          f'{shop.get_items()}')


if __name__ == "__main__":
    main()

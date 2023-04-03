class Request:
    def __init__(self, string):
        req = string.split()
        if req[0] not in ["забрать", "доставить"]:
            raise ValueError
        if len(req) != 7:
            raise ValueError
        if not req[1].isdigit():
            raise ValueError

        self._cmd_word = req[0]
        self._from: str = req[4]
        self._to: str = req[6]
        self._amount: int = int(req[1])
        self._product: str = req[2]

    def __repr__(self):
        return f'from = "{self._from}",\n' \
               f'to = "{self._to}",\n' \
               f'amount = "{self._amount}",\n' \
               f'product = "{self._product}"'

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product
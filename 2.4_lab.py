if __name__ == "__main__":
    # Write your solution here
    pass

class Guitar:
    def __init__(self, name: str, price: float, strings: int):
        """
            Создание и подготовка к работе объекта "Гитара"

            :param name: Название модели гитары
            :param price: Цена гитары
            :param strings: Количество струн

            Примеры:
            >>> guitar = Guitar("ER-2000", price=7500, strings=4)  # инициализация экземпляра класса
        """
        self.name = name
        self.price = price
        self.strings = strings

    def __str__(self):
        return f"Гитара '{self.name}', Цена '{self.price}'"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, manufacturer={self.price!r}, strings={self.strings!r})"

    def total_price(self) -> str:
        """
            Метод, опрделяющий общую цену покупки, в которую входит гитара и чехол для гитары

            :return: Общая цена покупки гитары с чехлом

            Примеры
            >>> guitar = Guitar("ER-2000", price=7500, strings=4)
            >>> guitar.total_price
        """
        guitar_case_price = 2500
        total_price = guitar_case_price + self.price
        return f"Общая цена покупки составляет '{total_price}'. В нее входит цена гитары '{self.price}' и цена чехла '{guitar_case_price}'."


    def classic(self) -> bool:
        """
           Метод, который проверяет является ли гитара классической шестиструнной

           :return: Является ли гитара классческой шестриструнной

           Примеры:
           >>> guitar = Guitar("ER-2000", price=7500, strings=4)
           >>> guitar.classic()
        """
    ...

class Acoustic(Guitar):
    def _init__(self, name: str, price:float, strings: int, wood_type: str):
        """
            Создание и подготовка к работе объекта "Акустическая гитара"

            :param name: Название модели гитары
            :param price: Цена гитары
            :param strings: Количество струн
            :param wood_type: Вид древесины

            Примеры
            >>> acoustic = Acoustic("ACT Pro", price=6500, strings=6, wood_type="maple")  # инициализация экземпляра класса
        """
        super().__init__()
        self.wood_type = wood_type

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self.price!r}, strings={self.strings!r}), wood_type={self.wood_type!r}"

    def total_price(self) -> str:
        """
            Метод, опрделяющий общую цену покупки, в которую входит гитара и чехол для гитары
            При покупке акустической гитары также понадобится гигрометр для ухода за древесиной гитары

            :return: Общая цена покупки вместе с гитарой, чехлом и гигрометром

            Примеры
            >>> acoustic = Acoustic("ACT Pro", price=6500, strings=6)
            >>> acoustic.total_price
        """
        guitar_case_price = 2500
        hygrometer_price = 1700
        total_price = guitar_case_price + hygrometer_price + self.price
        return f"Общая цена покупки составляет '{total_price}'. В нее входит цена гитары '{self.price}', цена чехла '{guitar_case_price}' и цена гигрометра '{hygrometer_price}'."



class Electronic(Guitar):
    def _init__(self, name: str, price: float, strings: int, connector: str):
        """
            Создание и подготовка к работе объекта "Электро гитара"

            :param name: Название модели гитары
            :param price: Цена гитары
            :param strings: Количество струн
            :param connector: Вид разъема для шнура

            Примеры
            >>> electronic = Electronic("Electro 5.0", price=1000, strings=6, connector="TRS Jack")  # инициализация экземпляра класса
        """
        super().__init__()
        self.connector = connector

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, manufacturer={self.price!r}, strings={self.strings!r}), connector={self.connector!r}"

    def total_price(self) -> str:
        """
            Метод, опрделяющий общую цену покупки, в которую входит гитара и чехол для гитары
            При покупке электронной гитары также понадобится электрический шнур для подключения к акустическим системам

            :return: Общая цена покупки вместе с гитарой, чехлом и шнуром

            Примеры
            >>> electronic = Electronic("Electro 5.0", price=1000, strings=6, connector="TRS Jack")
            >>> electronic.total_price
        """
        guitar_case_price = 2500
        cord_price = 1700
        total_price = guitar_case_price + cord_price + self.price
        return f"Общая цена покупки составляет '{total_price}'. В нее входит цена гитары '{self.price}', цена чехла '{guitar_case_price}' и цена шнура '{cord_price}'."



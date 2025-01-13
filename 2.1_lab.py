# TODO Написать 3 класса с документацией и аннотацией типов

import doctest



class construction:
    def __init__(self, bearing_capacity: float, external_load: float):
        """
        Создание и подготовка к работе объекта "Конструкция"

        :param bearing_capacity: Несущая способность контрукции
        :param external_load: Внешняя нагрузка

        Примеры:
        >>> building = construction(18000, 600)  # инициализация экземпляра класса
        """
        if not isinstance(bearing_capacity, (int, float)):
            raise TypeError("Значение несущей способности контрукции должно быть типа int или float")
        if bearing_capacity <= 0:
            raise ValueError("Значение несущей способности контрукции должно быть положительным числом")
        self.bearing_capacity = bearing_capacity

        if not isinstance(external_load, (int, float)):
            raise TypeError("Значение усилия внешней нагрузки должно быть int или float")
        if external_load < 0:
            raise ValueError("Значение усилия внешней нагрузки не может быть отрицательным числом")
        self.external_load = external_load


    def breaking_load(self) -> bool:
        """
        Функция которая проверяет является ли внешняя нагрузка разрушающей

        :return: Является ли внешняя нагрузка разрушающей

        Примеры:
        >>> building = construction(18000, 600)
        >>> building.breaking_load()
        """
        ...


    def extra_load(self, extra: float) -> None:
        """
        Увеличение нагрузки на конструкцию.
        :param extra: Величина увеличения внешней нагрузки

        :raise ValueError: Если суммарная нагрузка на кострукцию превышает несущую
        способность, то вызываем ошибку

        Примеры:
        >>> building = construction(18000, 600)
        >>> building.extra_load(1000)
        """
        if not isinstance(extra, (int, float)):
            raise TypeError("Значение добавляемой нагрузки должно быть типа int или float")
        if extra < 0:
            raise ValueError("Значение добавляемой нагрузки должно быть положительным числом")
        ...


    def load_relief(self, relief: float) -> None:
        """
        Снятие нагрузки.

        :param relief: Величина снимаемой нагрузки
        :raise ValueError: Если величина снимаемой нагрузки превышает суммарную внешнюю
        нагрузку на конструкцию, то вызываем ошибку

        :return: Величина остаточной нагрузки на кострукцию

        Примеры:
        >>> building = construction(18000, 1600)
        >>> building.load_relief(200)
        """
        ...



class school_class:
    def __init__(self, girl: int, boy: int):
        """
        Создание и подготовка к работе объекта "Школьный класс"

        :param girl: Количество девочек в классе
        :param boy: Количество мальчиков в классе

        Примеры:
        >>> seventh_a = school_class(7, 3)  # инициализация экземпляра класса
        """
        if not isinstance(girl, (int)):
            raise TypeError("Количество девочек должно быть целым числом, т.е. типа int")
        if girl <= 0:
            raise ValueError("Количество девочек должно быть положительным числом")
        self.girl = girl

        if not isinstance(boy, (int)):
            raise TypeError("Количество мальчиков должно быть целым числом, т.е. типа int")
        if boy < 0:
            raise ValueError("Количество мальчиков не может быть отрицательным числом")
        self.boy = boy


    def percentage(self) -> float:
        """
        Функция которая вычисляет процентное соотношение
        девочек и мальчиков в классе

        :return: процент соотношения

        Примеры:
        >>> seventh_a = school_class(7, 3)
        >>> seventh_a.percentage()
        """
        ...


    def increase_in_girls(self, girls: int) -> None:
        """
        Увеличение количества девочек в классе.
        :param girls: Количество добавленных в класс девочек

        :raise ValueError: Если общее количество учеников больше 31, то
        вызываем ошибку

        Примеры:
        >>> seventh_a = school_class(7, 3)
        >>> seventh_a.increase_in_girls(15)
        """
        if not isinstance(girls, (int)):
            raise TypeError("Количество девочек должно быть целым числом, т.е. типа int")
        if girls < 0:
            raise ValueError("Количество девочек должно быть положительным числом")
        ...


    def deduction(self, studies: int) -> None:
        """
        Отчисление учеников.

        :param studies: Количество выбывших из класса учеников
        :raise ValueError: Если количество отчисленных превышает общее количество учеников в классе,
        то выдаем ошибку

        :return: Общее количество отсавшихся в классе учеников

        Примеры:
        >>> seventh_a = school_class(22, 3)
        >>> seventh_a.deduction(2)
        """
        ...



class color_palette :
    def __init__(self, name_color: str, number_of_cans: int):
        """
        Создание и подготовка к работе объекта "Цветовая палитра"

        :param name_color: Название оттенка из каталога магазина
        :param number_of_cans: Количество банок с данным оттенком краски

        Примеры:
        >>> lerya_merlen = color_palette("blue", 3)  # инициализация экземпляра класса
        """
        if not isinstance(name_color, (str)):
            raise TypeError("Название оттенка краски должно быть типа str")
        self.name_color = name_color

        if not isinstance(number_of_cans, (int)):
            raise TypeError("Количество банок с краской должно быть целым числом, т.е. типа int")
        if number_of_cans < 0:
            raise ValueError("Количество банок с краской не может быть отрицательным числом")
        self.number_of_cans = number_of_cans


    def color_mixing(self, name_color_1: str, name_color_2: str, name_color: str, cans: int) -> None:
        """
        Получение нового оттенка благодаря смешению двух цветов
        :param name_color_1: Первый цвет для смешения
        :param name_color_2: Второй цвет для смешения
        :param name_color: Название нового цвета
        :param cans: Количество банок с новым оттенком краски

        :raise ValueError: Если названия первого и/или второго цвета отсутсвтуют, то
        вызываем ошибку

        Примеры:
        >>> lerya_merlen = color_palette("blue", 3)
        >>> lerya_merlen.color_mixing("yelloy", "blue", "green", 20)
        """
        if not isinstance(name_color_1, (str)):
            raise TypeError("Название оттенка должно быть типа str")
        if not isinstance(name_color_2, (str)):
            raise TypeError("Название оттенка должно быть типа str")
        if not isinstance(name_color, (str)):
            raise TypeError("Название оттенка должно быть типа str")
        if not isinstance(cans, (int)):
            raise TypeError("Количество банок должно быть целым числом, т.е. типа int")
        if cans < 0:
            raise ValueError("Количество банок должно быть положительным числом")
        ...


    def supply(self, name_color: str, number_of_cans: int) -> None:
        """
        Поставка банок с краской в магазин.
        :param name_color: Название поставляемого цвета
        :param number_of_cans: Количество банок поставляемого цвета краски

        Примеры:
        >>> lerya_merlen = color_palette("blue", 3)
        >>> lerya_merlen.supply("yelloy", 7)
        """
        if not isinstance(name_color, (str)):
            raise TypeError("Название оттенка должно быть типа str")
        if not isinstance(number_of_cans, (int)):
            raise TypeError("Количество банок должно быть целым числом, т.е. типа int")
        if number_of_cans < 0:
            raise ValueError("Количество банок должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

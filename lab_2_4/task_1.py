class FuelRocket:
    """Базовый класс топливной системы одноступенчатой ракеты"""
    def __init__(self, mass_of_fuel: int, mass_of_oxidant: int):
        """Создание топливной системы одноступенчатой ракеты
        :param mass_of_fuel: Масса горючего в баке в тоннах
        :param mass_of_oxidant: Масса окислителя в баке в тоннах

        Пример:
        >>> rocket = FuelRocket(100, 200)
        """
        self.mass_of_fuel = mass_of_fuel
        self.mass_of_oxidant = mass_of_oxidant

    def __str__(self):
        return f"Ракета одноступенчатая. Масса горючего - {self.mass_of_fuel}. Масса окислителя - {self.mass_of_oxidant}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mass_of_fuel={self.mass_of_fuel}, mass_of_oxidant={self.mass_of_oxidant})"

    def add_fuel(self, extra_fuel: int):
        """Доливка горючего в бак
        :param extra_fuel: Масса дополнительного горючего в бак в тоннах
        :return: Суммарная масса топлива

        Пример:
        >>> rocket = FuelRocket(100, 200)
        >>> rocket.add_fuel(25)
        """
        self.mass_of_fuel += extra_fuel

    def blowdown_of_system(self) -> bool:
        """Продувка топливной системы азотом
        :return: Отчет на подачу команды продувки топливной системы
        """


class TwoStage(FuelRocket):
    """Дочерний класс топливной системы одноступенчатой ракеты - двухступенчатая ракета.
    Метод blowdown_of_system унаследован"""
    def __init__(self, mass_of_1_fuel: int, mass_of_1_oxidant: int, mass_of_2_fuel: int, mass_of_2_oxidant: int):
        """Создание топливной системы двухступенчатой ракеты
        :param mass_of_1_fuel: Масса горючего в баке первой ступени в тоннах
        :param mass_of_1_oxidant: Масса окислителя в баке первой ступени в тоннах
        :param mass_of_2_fuel: Масса горючего в баке второй ступени в тоннах
        :param mass_of_2_oxidant: Масса окислителя в баке второй ступени в тоннах
        """
        super().__init__(mass_of_fuel=mass_of_1_fuel, mass_of_oxidant=mass_of_1_oxidant)
        self.mass_of_1_fuel = mass_of_1_fuel
        self.mass_of_1_oxidant = mass_of_1_oxidant
        self.mass_of_2_fuel = mass_of_2_fuel
        self.mass_of_2_oxidant = mass_of_2_oxidant

    def __str__(self):
        """Метод перегружен из-за необходимости вывода характеристик второй ступени"""
        return f"Ракета двухступенчатая.\n" \
               f"Масса горючего 1 ступени - {self.mass_of_1_fuel}. Масса окислителя 1 ступени - {self.mass_of_1_oxidant}\n" \
               f"Масса горючего 2 ступени - {self.mass_of_2_fuel}. Масса окислителя 2 ступени - {self.mass_of_2_oxidant}"

    def __repr__(self):
        """Метод перегружен из-за необходимости вывода суммарной характеристики ракеты"""
        return f"{self.__class__.__name__}(mass_of_fuel={self.mass_of_1_fuel + self.mass_of_2_fuel}," \
               f" mass_of_oxidant={self.mass_of_1_oxidant + self.mass_of_2_oxidant})"

    def add_fuel(self, extra_1_fuel: int = 0, extra_2_fuel: int = 0):
        """Метод перегружен из-за возможности доливать горючее в бак второй ступени
        :param extra_1_fuel: Масса дополнительного горючего в бак первой ступени в тоннах
        :param extra_2_fuel: Масса дополнительного горючего в бак второй ступени в тоннах
        :return: Суммарная масса топлива в каждом баке
        """
        super().add_fuel(extra_fuel=extra_1_fuel)
        self.mass_of_1_fuel += extra_1_fuel
        self.mass_of_2_fuel += extra_2_fuel


if __name__ == "__main__":
    # проверка методов
    rocket_one = FuelRocket(100, 200)
    rocket_one.add_fuel(25)
    print(rocket_one)
    rocket_two = TwoStage(100, 200, 200, 300)
    rocket_two.add_fuel(50)
    print(rocket_two)
    print(repr(rocket_two))
    pass

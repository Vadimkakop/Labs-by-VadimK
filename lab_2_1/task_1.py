import doctest
from typing import Union


class Rocket:
    def __init__(self, mass_of_rocket: Union[int, float], mass_of_payload: Union[int, float]):
        """
        Создание объекта "ракетоноситель"
        :param mass_of_rocket: Стартовая масса ракеты
        :param mass_of_payload: Масса полезной нагрузки

        Пример:
        >>> ProtonM = Rocket(705, 23.7)
        """
        if not isinstance(mass_of_rocket, (int, float)):
            raise TypeError("Стартовая масса ракеты должна быть типа int или float")
        if mass_of_rocket <= 0:
            raise ValueError("Стартовая масса ракеты не может быть отрицательным числом")
        self.mass_of_rocket = mass_of_rocket

        if not isinstance(mass_of_payload, (int, float)):
            raise TypeError("Масса полезной нагрузки должна быть int или float")
        if mass_of_payload < 0:
            raise ValueError("Масса полезной нагрузки не может быть отрицательным числом")
        if mass_of_payload >= mass_of_rocket:
            raise ValueError('Масса полезной нагрузки не может быть больше стартовой массы ракеты')
        self.mass_of_payload = mass_of_payload

    def check_of_first_stage_separation(self) -> bool:
        """
        Функция которая фиксирует отрыв первой ступени ракетоносителя
        :return: Отделилась ли первая ступень
        """
        ...

    def launch_of_second_stage(self) -> bool:
        """
        Функция которая фиксирует запуск второй ступени ракетоносителя
        :return: Запустилась ли двигательная установка второй ступени
        """
        ...


class StaffDepartment:
    def __init__(self, numbers_of_employees: int, sum_salary: int, sum_experience: int):
        """
        Создание объекта "отдел кадров"
        :param numbers_of_employees: Число сотрудников в штате
        :param sum_salary: Суммарная зарплата
        :param sum_experience: Суммарный стаж работы в фирме

        Пример:
        >>> HornsHooves = StaffDepartment(5, 100, 20)
        """
        if not isinstance(numbers_of_employees, int):
            raise TypeError("Число работников должно быть типа int")
        if numbers_of_employees <= 0:
            raise ValueError("Число работников не может быть отрицательным числом")
        self.numbers_of_employees = numbers_of_employees

        if not isinstance(sum_salary, int):
            raise TypeError("Суммарная зарплата должна быть типа int")
        if sum_salary <= 0:
            raise ValueError("Суммарная зарплата не может быть отрицательным числом")
        self.sum_salary = sum_salary

        if not isinstance(sum_experience, int):
            raise TypeError("Суммарный стаж должен быть типа int")
        if sum_experience <= 0:
            raise ValueError("Суммарный стаж не может быть отрицательным числом")
        self.sum_experience = sum_experience

    def average_salary(self) -> float:
        """
        Функция которая вычисляет среднюю зарплату штата сотрудников
        :return: Средняя зарплата штата

        Пример:
        >>> staff = StaffDepartment(5, 100, 20)
        >>> staff.average_salary()
        """
        ...

    def prize(self, average_salary) -> float:
        """
        Функция которая вычисляет премию за выслугу лет
        :param average_salary: Средняя зарплата
        :raise ValueError: Премия выше установленного порога
        :return: Премия за выслугу лет

        Пример:
        >>> staff = StaffDepartment(5, 100, 20)
        >>> staff.prize(staff.average_salary())
        """
        ...


class Vector:
    def __init__(self, coordinate_of_start: list, coordinate_of_end: list):
        """
        Создание объекта "вектор"
        :param coordinate_of_start: Координаты по осям x и y точки начала вектора
        :param coordinate_of_end: Координаты по осям x и y точки конца вектора

        Примеры:
        >>> vector1 = Vector([-2, 5], [5, 1])
        >>> vector2 = Vector([0, 0], [5, 3])
        """
        for i, j in coordinate_of_start, coordinate_of_end:
            if not isinstance(i, (int, float)) or not isinstance(j, (int, float)):
                raise TypeError("Координаты должно быть типа int или float")
        self.coordinate_of_start = coordinate_of_start
        self.coordinate_of_end = coordinate_of_end

    def len_of_vector(self):
        """
        Функция которая вычисляет длину вектора
        :return: Длина вектора

        Пример:
        >>> vector1 = Vector([-2, 5], [5, 1])
        >>> vector1.len_of_vector()
        """
        ...

    def multiplication_by_number(self, number):
        """
        Функция которая умножает вектор на число
        :param number: Число на которое нужно умножить вектор
        :return: Вектор, умноженный на число

        Пример:
        >>> vector1 = Vector([-2, 5], [5, 1])
        >>> vector1.multiplication_by_number(5)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

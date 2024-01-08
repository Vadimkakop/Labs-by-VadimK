class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._name

    @property
    def author(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self._pages = pages

    @property
    def pages(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self._duration = duration

    @property
    def duration(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает продолжительность аудио книги."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудио книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудио книги должна быть положительным числом")
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

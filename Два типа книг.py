class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name

        @property
        def name(self) -> str:
            return self._name

        self.author = author

        @property
        def autor(self) -> str:
            return self._autor

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int, ):
        super().__init__(name, author)
        self._pages = pages

    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages
    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.pages!r})'

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    @property
    def duration(self) -> float:
        """Возвращает продолжительнсть книги."""
        return self._duration
    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает продолжительность книги."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должа быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность книги {self.duration}"

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.duration!r})'



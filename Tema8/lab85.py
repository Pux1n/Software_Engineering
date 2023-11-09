class Shape:  # Создаем класс Shape
    def area(self):  # Создаем пустой метод для подсчета площади
        pass


class Rectangle(Shape):  # Создаем дочерний класс Rectangle от Shape
    def __init__(self, width, height):  # Инициализируем атрибуты
        self.width = width  # атрибут ширины
        self.height = height  # атрибут высоты

    def area(self):  # Создаем метод для подсчета площади
        return self.width * self.height  # Возвращает площадь прямоугольника


class Circle(Shape):  # Создаем дочерний класс Circle от Shape
    def __init__(self, radius):  # Инициализируем атрибуты
        self.radius = radius  # атрибут радиуса

    def area(self):  # Создаем метод для подсчета площади
        return 3.14 * self.radius * self.radius  # Возвращает площадь круга


shapes = [Rectangle(5, 4), Circle(3)]  # Создаем массив фигур
for shape in shapes:  # Проходимся по массиву фигур
    print(shape.area())  # Выводим их площадь

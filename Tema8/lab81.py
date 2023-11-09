class Car:  # Создаем класс машины.
    def __init__(self, make, model):  # Инициализируем атрибуты объекта класса
        self.make = make  # Определяем атрибут производитель
        self.model = model  # Определяем атрибут модель


my_car = Car("Toyota", "Corolla")  # Создаем объект класса Car и присваиваем ему атрибуты

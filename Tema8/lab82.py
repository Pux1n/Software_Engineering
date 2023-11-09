class Car:  # Создаем класс машины.
    def __init__(self, make, model):  # Инициализируем атрибуты объекта класса
        self.make = make  # Определяем атрибут производитель
        self.model = model  # Определяем атрибут модель

    def drive(self):  # Добавляем метод класса для езды
        print(f"Driving the {self.make} {self.model}")  # Едем


my_car = Car("Toyota", "Corolla")  # Создаем объект класса Car и присваиваем ему атрибуты
my_car.drive()

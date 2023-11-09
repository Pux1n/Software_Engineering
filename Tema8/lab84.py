class Car:  # Создаем класс машины.
    def __init__(self, make, model):  # Инициализируем атрибуты объекта класса
        self._make = make  # Определяем защищенный атрибут производитель
        self.__model = model  # Определяем приватный атрибут модель

    def drive(self):  # Добавляем метод класса для езды
        print(f"Driving the {self._make} {self.__model}")  # Едем


my_car = Car("Toyota", "Corolla")  # Создаем объект класса Car и присваиваем ему атрибуты
print(my_car._make)  # Вызываем защищенный атрибут
my_car.drive()  # Едем

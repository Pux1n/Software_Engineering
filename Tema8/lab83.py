class Car:  # Создаем класс машины.
    def __init__(self, make, model):  # Инициализируем атрибуты объекта класса
        self.make = make  # Определяем атрибут производитель
        self.model = model  # Определяем атрибут модель

    def drive(self):  # Добавляем метод класса для езды
        print(f"Driving the {self.make} {self.model}")  # Едем


class ElectricCar(Car):  # Создаем дочерний класс машины.
    def __init__(self, make, model, battery_capacity):  # Инициализируем атрибуты объекта класса
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):  # Добавляем метод класса для заправки
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")


my_electric_car = ElectricCar("Tesla", "Model S", 75)  # Создаем объект класса ElectricCar
my_electric_car.drive()  # Едем
my_electric_car.charge()  # Заряжаем

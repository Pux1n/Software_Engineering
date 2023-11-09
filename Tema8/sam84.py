class Animal:
    def __init__(self, type, name):
        self._name = name
        self.__type = type

    def eat(self):
        print(f"{self.__type} {self._name} ест.")


murzik = Animal("Кот", "Мурзик")
print(murzik._name)
# print(murzik.__type) # Ошибка
murzik.eat()

class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def eat(self):
        print(f"{self.type} {self.name} ест.")


murzik = Animal("Кот", "Мурзик")
murzik.eat()

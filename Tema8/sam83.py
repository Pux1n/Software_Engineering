class Animal:
    def __init__(self, type, name):
        self.name = name
        self.type = type

    def eat(self):
        print(f"{self.type} {self.name} ест.")


class Cat(Animal):
    def __init__(self, name):
        super().__init__("Кот", name)
        self.name = name

    def purr(self):
        print(f"Кот {self.name} мурчит.")


murzik = Cat("Мурзик")
murzik.eat()
murzik.purr()

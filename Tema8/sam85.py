class Animal:
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        print("Собака бегает")


class Fish(Animal):
    def move(self):
        print("Рыба плавает")


class Bird(Animal):
    def move(self):
        print("Птица летает")


animals = [Dog(), Fish(), Bird()]
for animal in animals:
    animal.move()

class Tomato:
    states = ('отсутствует', 'цветение', 'зеленый', 'красный')

    def __init__(self, index):
        self._index = index  # Защищенный атрибут.
        self._state = self.states[0]  # Защищенный атрибут.

    # Метод созревания помидора.
    def grow(self):
        # Если состояние не "красное", то повышает текущее состояние на 1.
        if self.states.index(self._state) + 1 <= 3:
            self._state = self.states[self.states.index(self._state) + 1]
        # Иначе оставляет красным.
        else:
            self._state = self.states[3]

    # Метод проверки спелости помидора.
    def is_ripe(self):
        if self._state == 'красный':
            return True
        else:
            return False


class TomatoBush:
    def __init__(self, number_tomatoes):
        self.tomatoes = []  # Создаем пустой список помидоров.
        for i in range(number_tomatoes - 1):  # Проходимся от 0 до числа помидоров минус 1
            tomato = Tomato(i)  # Создаем экземпляр помидора с индексом i
            self.tomatoes.append(tomato)  # Добавляем помидор в список.

    # Метод созревания всех помидоров.
    def grow_all(self):
        # Проход по помидорам в списке.
        for tomato in self.tomatoes:
            tomato.grow()  # Вызов метода созревания.

    # Метод проверки спелости всех помидоров.
    def all_are_ripe(self):
        # Возвращает True, если все помидоры созрели, и False, если не все.
        return all(tomato.is_ripe() is True for tomato in self.tomatoes)

    # Метод чистки списка помидоров.
    def give_away_all(self):
        self.tomatoes = []  # Очищает список


class Gardener:
    def __init__(self, name, tomato_bush):
        self.name = name  # Публичный атрибут.
        self._plant = tomato_bush  # Защищенный атрибут.

    # Метод работы.
    def work(self):
        if not self._plant.tomatoes:  # Проверка на пустой куст.
            print("Куст пуст - нечего поливать!")
        else:
            self._plant.grow_all()  # Вызов метода созревания всех помидоров.
            print(f"{self.name} полил помидоры и они выросли.")

    # Метод сбора урожая.
    def harvest(self):
        if not self._plant.tomatoes:  # Проверка на пустой куст.
            print("Куст пуст - нечего собирать!")
        else:
            if self._plant.all_are_ripe():  # Вызов метода проверки на спелость всех помидоров.
                self._plant.give_away_all()  # Вызов метода чистки помидоров.
                print("Урожай собран.")
            else:
                print("Еще не все помидоры созрели.")

    @staticmethod  # Декоратор статистического метода.
    def knowledge_base():  # Метод для вывода справки по садоводству.
        print("Уход за томатами заключается в окучивании, рыхлении почвы, подкормках и поливах, \nформировании куста и "
              "своевременной борьбе с болезнями и вредителями.Томаты следует \nполивать исключительно под корень, "
              "особенно во время цветения.\n")


# Тесты.
Gardener.knowledge_base()
t_bush = TomatoBush(12)
gardener = Gardener("Ваня", t_bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()

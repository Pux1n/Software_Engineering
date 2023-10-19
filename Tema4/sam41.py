# импорт функции datetime из модуля datetime
from datetime import datetime
# импорт функции sqrt из модуля math
from math import sqrt


def main(**kwargs):
    """Функция, принимающая кортежи"""

    # проход по входному кортежу
    for key in kwargs.items():
        # В результат записывается кв. корень из
        # суммы квадратов первого и второго элемента кортежа.
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)

        print(result)  # Вывод результата


if __name__ == '__main__':
    """Точка входа в программу"""

    start_time = datetime.now()  # Записывается текущая точка во времени.

    # Вызов функции main, принимающей пять кортежей
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )

    # Записывается разница текущего времени от start_time.
    time_costs = datetime.now() - start_time
    # Вывод времени выполнения программы.
    print(f"Время выполнения программы - {time_costs}")

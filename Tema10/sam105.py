class NotIntError(Exception):
    def __init__(self, message='Ошибка: в аргументах функции введен не целочисленный параметр.'):
        self.message = message
        super().__init__(self.message)


def summ(*args):
    nums = args
    result = 0
    for num in nums:
        if isinstance(num, int):
            result += num
        else:
            raise NotIntError()
    return result


try:
    print(summ(1, 2, 3, 4))
except NotIntError as e:
    print(e)

try:
    print(summ(2, 4, 4, 'a', 'f'))
except NotIntError as e:
    print(e)

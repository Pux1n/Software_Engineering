import time


def time_of(func):
    def input_func():
        start_time = time.time()
        result = func()
        end_time = time.time()
        result_time = end_time - start_time
        print(f"\nВремя выполнения: {result_time} сек")
        return result
    return input_func


@time_of
def fibonacci():
    fib1 = fib2 = 1

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end='')


if __name__ == '__main__':
    fibonacci()

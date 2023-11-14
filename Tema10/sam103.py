def plus_two():
    try:
        b = int(input("Введите число, которое нужно сложить с 2: "))
        result = 2 + b
        return result
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


print(plus_two())
print(plus_two())
print(plus_two())

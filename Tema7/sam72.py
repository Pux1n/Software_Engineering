def input_expenses():
    name = input("\nВведите название расходов: ")
    amount = float(input("Введите сумму расходов: "))

    with open('expenses.txt', 'a', encoding='utf-8') as f:
        f.write(f"{name}: {amount} руб.\n")


def display_expenses():
    try:
        with open('expenses.txt', 'r', encoding='utf-8') as f:
            expenses = f.read()
            print("\nСуществующие расходы:")
            print(expenses)
    except FileNotFoundError:
        print("\nФайл не найден.")


def main():
    while True:
        print("\n1. Ввести информацию о расходах")
        print("2. Вывести существующие расходы")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            input_expenses()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            break
        else:
            print("\nВведите от 1 до 3!")


if __name__ == "__main__":
    main()

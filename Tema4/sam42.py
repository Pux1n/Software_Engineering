import random


def main():
    x = random.randint(1, 6)
    print(x)
    if x == (5 or 6):
        print("Вы победили")
    elif x == (1 or 2):
        print("Вы проиграли")
    else:
        main()


if __name__ == '__main__':
    main()

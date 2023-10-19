from random import randint


def main():
    x = randint(1, 6)
    print(x)
    if x in (5, 6):
        print("Вы победили")
    elif x in (1, 2):
        print("Вы проиграли")
    else:
        main()


if __name__ == '__main__':
    main()

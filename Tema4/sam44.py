
def main(*args):
    mean = sum(args)
    print(mean)


if __name__ == '__main__':
    main(1, 2, 3, 4, 5)
    main(1, 2)
    main(5)

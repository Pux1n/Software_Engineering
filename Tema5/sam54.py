def fix(lst):
    lst2 = []
    for i in lst:
        if i == 2:
            continue
        elif i == 3:
            lst2.append(4)
        else:
            lst2.append(i)
    print(lst2)


fix([2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4])
fix([4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4])
fix([5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4])

def to_set(lst):
    my_set = set()
    temp = 0
    lst.sort()
    for i in lst:
        if i not in my_set:
            temp = 1
            my_set.add(i)
        else:
            temp += 1
        if temp > 1:
            dop = str(i) * temp
            my_set.add(dop)
    print(my_set)


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

to_set(list_1)
to_set(list_2)
to_set(list_3)

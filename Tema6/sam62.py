def remove(tpl, value):
    if value not in tpl:
        return tpl
    else:
        i = tpl.index(value)
        new_tpl = tpl[:i] + tpl[i + 1:]
        return new_tpl


print(remove((1, 2, 3), 1))
print(remove((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove((2, 4, 6, 6, 4, 2), 9))

def count_string(tpl, string):
    counts = {}
    for element in tpl:
        count = string.count(str(element))
        counts[element] = count
    return counts


print(count_string((1, 2, 0, 'm', 'e', 20), "Hello world. My name is Andrey, I'm 20"))
print(count_string(('t', 'e', 99, '2'), "Test number 2"))
print(count_string((1, 2, 123, '.', '123'), "123.4 1 2 3 4"))

def office(tpl, id):
    if id not in tpl:
        return ()
    first_id = None
    second_id = None
    index = 0
    for i in tpl:
        if i == id:
            if first_id is None:
                first_id = index
            else:
                second_id = index+1
                break
        index += 1
    result = tpl[first_id:second_id]
    return result


print(office((1, 2, 3), 8))
print(office((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(office((1, 2, 8, 5, 1, 2, 9), 8))

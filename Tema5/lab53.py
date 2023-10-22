def replace(input_list):
    memory = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = memory

    return input_list


print(replace([1, 2, 3, 4, 5]), '\n')

# в две строчки (в три)
lis = [1, 2, 3, 4, 5]
lis[0], lis[-1] = lis[-1], lis[0]
print(lis)

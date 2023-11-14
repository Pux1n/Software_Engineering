def half(func):
    def output_func(*args):
        result = func(*args) / 2
        return result
    return output_func


@half
def summ(*args):
    nums = args
    result = 0
    for num in nums:
        result += num
    return result


@half
def mult(*args):
    nums = args
    result = 1
    for num in nums:
        result *= num
    return result


print(summ(1, 2, 3, 4))
print(mult(1, 2, 3, 4))

def fib(a, b, n):
    for i in range(n):
        current = a
        a, b = b, a + b
        yield current


result = 0
for f in fib(1, 1, 200):
    result = f

print(result)

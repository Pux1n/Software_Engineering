def fib(a, b, n):
    for i in range(n):
        current = a
        a, b = b, a + b
        yield current


with open("fib.txt", 'a', encoding='utf-8') as f:
    result = 0
    for s in fib(1, 1, 200):
        f.write(f"{s}\n")

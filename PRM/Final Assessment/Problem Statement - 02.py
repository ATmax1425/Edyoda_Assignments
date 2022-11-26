def nth_fib(n):
    n -= 1
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n-1):
        print(b)
        a, b = b, a + b
    return b


num = int(input())
print(nth_fib(num))

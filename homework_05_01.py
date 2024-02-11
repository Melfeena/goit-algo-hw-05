# Створюємо функцію fibonacci зі словником для запису в кеш
def caching_fibonacci():
    cache = dict()

# Обчислюємо саму функцію, результати передаєм в словник
    def fibonacci(n):
        if n <= 0: return 0
        if n == 1: return 1
        if n in cache: return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі, виводимо результати
print(fib(10))
print(fib(15))
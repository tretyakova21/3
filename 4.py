def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Пример использования
n_input = int(input("Введите натуральное число N: "))
result_factorial = factorial(n_input)
print("Факториал числа N:", result_factorial)

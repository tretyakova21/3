def sum_of_numbers(n):
    return sum(range(1, n + 1))

# Пример использования
n_input = int(input("Введите число N: "))
result_sum = sum_of_numbers(n_input)
print("Сумма всех чисел от 1 до N:", result_sum)

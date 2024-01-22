def count_digits(number):
    return len(str(abs(number)))

# Пример использования
number_input = int(input("Введите целое число: "))
result_digits = count_digits(number_input)
print("Количество цифр в числе:", result_digits)

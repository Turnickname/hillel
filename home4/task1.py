input_string = input("Введіть рядок: ")

letters = 0
digits = 0

for char in input_string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

# Виводимо кількість літер і цифр на екран
print(f"Кількість літер: {letters}")
print(f"Кількість цифр: {digits}")

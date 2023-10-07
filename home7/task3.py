def sum_range(a, b):
    if a > b:
        return 0
    else:
        return a + sum_range(a + 1, b)

a = int(input("Введіть a: "))
b = int(input("Введіть b: "))

result = sum_range(a, b)
print(f"Сума чисел у діапазоні від {a} до {b} дорівнює {result}")

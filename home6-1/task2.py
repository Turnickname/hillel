import random

even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []

random_list = [random.randint(-100, 100) for _ in range(20)]

for num in random_list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

    if num < 0:
        negative_numbers.append(num)
    elif num > 0:
        positive_numbers.append(num)

print("Список парних чисел:", even_numbers)
print("Список непарних чисел:", odd_numbers)
print("Список негативних чисел:", negative_numbers)
print("Список позитивних чисел:", positive_numbers)

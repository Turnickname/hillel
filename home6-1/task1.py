import random

random_list = [random.randint(-100, 100) for _ in range(20)]

sum_negative = sum(num for num in random_list if num < 0)

sum_even = sum(num for num in random_list if num % 2 == 0)

sum_odd = sum(num for num in random_list if num % 2 != 0)

min_index = random_list.index(min(random_list))
max_index = random_list.index(max(random_list))

product_multiple_of_3 = 1
for i in range(0, len(random_list), 3):
    product_multiple_of_3 *= random_list[i]

product_between_min_max = 1
for i in range(min(min_index, max_index) + 1, max(min_index, max_index)):
    product_between_min_max *= random_list[i]

positive_indices = [i for i, num in enumerate(random_list) if num > 0]
if len(positive_indices) >= 2:
    first_positive_index = positive_indices[0]
    last_positive_index = positive_indices[-1]
    sum_between_positive = sum(random_list[first_positive_index + 1:last_positive_index])
else:
    sum_between_positive = 0


print("Сума негативних чисел:", sum_negative)
print("Сума парних чисел:", sum_even)
print("Сума непарних чисел:", sum_odd)
print("Добуток елементів з кратними індексами 3:", product_multiple_of_3)
print("Добуток елементів між мінімальним і максимальним елементами:", product_between_min_max)
print("Сума елементів між першим і останнім позитивними елементами:", sum_between_positive)

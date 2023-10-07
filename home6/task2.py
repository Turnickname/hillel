def find_minimum(numbers):
    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

    return minimum

my_list = [5, 2, 8, 1, 4]
min_value = find_minimum(my_list)
print("Мінімальний елемент у списку:", min_value)

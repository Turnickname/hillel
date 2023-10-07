def multiply_elements(numbers):
    result = 1

    for num in numbers:
        result *= num

    return result

my_list = [2, 3, 4, 5]
result = multiply_elements(my_list)
print("Добуток елементів :", result)

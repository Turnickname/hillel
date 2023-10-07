def power_elements(numbers, exponent):
    result_list = []
    for num in numbers:
        result = num ** exponent
        result_list.append(result)
    return result_list

my_list = [2, 3, 4, 5]
exponent = 2
result = power_elements(my_list, exponent)
print("Список після обчислення ступеня:", result)

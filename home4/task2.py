input_string = input("введіть рядок:")

input_string_char = input("введіть пошуковий символ:")
i = 0
for char in input_string:
    if input_string_char == char:
        i += 1

results_string = (f'в цьому радяку "{input_string}" знайдено "{input_string_char}" в кількості {i}')
print(results_string)

input_string = input("Введіть рядок: ")

third_char = input_string[2]
print("1. Третій символ рядка:", third_char)

penultimate_char = input_string[-2]
print("2. Передостанній символ рядка:", penultimate_char)

first_five_chars = input_string[:5]
print("3. Перші п'ять символів рядка:", first_five_chars)

without_last_two_chars = input_string[:-2]
print("4. Рядок без двох останніх символів:", without_last_two_chars)

even_chars = input_string[::2]
print("5. Символи з парними індексами:", even_chars)

odd_chars = input_string[1::2]
print("6. Символи з непарними індексами:", odd_chars)

reversed_string = input_string[::-1]
print("7. Рядок в зворотному порядку:", reversed_string)

every_other_char_reversed = input_string[-1::-2]
print("8. Символи через один в зворотному порядку:", every_other_char_reversed)

string_length = len(input_string)
print("9. Довжина рядка:", string_length)

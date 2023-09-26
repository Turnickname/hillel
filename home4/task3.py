input_string = input("Введіть рядок: ")
search_word = input("Введіть слово для пошуку: ")
replace_word = input("Введіть слово для заміни: ")

results_string = input_string.replace(search_word, replace_word)
print(f"Результат: {results_string}")

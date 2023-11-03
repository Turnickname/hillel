with open('ваш_файл.txt', 'r') as file:
    content = file.read()

words = content.split()

word_count = len(words)

print(f"Кількість слів у файлі: {word_count}")

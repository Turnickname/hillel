with open('вхідний_файл.txt', 'r') as input_file:
    content = input_file.read()

words = content.split()

filtered_words = [word for word in words if len(word) >= 7]

result = ' '.join(filtered_words)

with open('новий_файл.txt', 'w') as output_file:
    output_file.write(result)

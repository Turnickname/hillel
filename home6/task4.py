def remove_element(input_list, target):
    count_removed = 0

    while target in input_list:
        input_list.remove(target)
        count_removed += 1

    return count_removed

my_list = [2, 3, 4, 2, 5, 2, 6]
target_element = 2
removed_count = remove_element(my_list, target_element)
print("Кількість видалених елементів:", removed_count)
print("Список після видалення:", my_list)

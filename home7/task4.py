import random
def find_min_sequence_position(arr):
    min_sum = float('inf')
    min_position = -1

    for i in range(len(arr) - 9):
        current_sum = sum(arr[i:i+10])

        if current_sum < min_sum:
            min_sum = current_sum
            min_position = i

    return min_position

random_list = [random.randint(1, 100) for _ in range(100)]

position = find_min_sequence_position(random_list)

print(f"Початкова позиція послідовності з мінімальною сумою: {position}")

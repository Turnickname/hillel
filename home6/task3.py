def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count

my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_count = count_primes(my_list)
print("Кількість простих чисел у списку:", prime_count)

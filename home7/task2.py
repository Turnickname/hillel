def print_stars(n):
    # якщо н = 0
    if n == 0:
        return
    print("*", end="")
    print_stars(n - 1)

n = int(input("Введіть кількість зірок: "))

print_stars(n)

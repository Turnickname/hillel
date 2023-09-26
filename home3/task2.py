try:
    num1 = int(input("Введіть перше число: "))
    num2 = int(input("Введіть друге число: "))

    if num1 == num2:
        print("Введені числа рівні.")
    else:
        if num1 < num2:
            print(f"Числа у порядку зростання: {num1}, {num2}")
        else:
            print(f"Числа у порядку зростання: {num2}, {num1}")

except ValueError:
    print("Введіть коректні числа.")

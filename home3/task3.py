try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    operation = input("Введіть математичну операцію (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Помилка: Ділення на нуль неможливе.")
            result = None
    else:
        print("Помилка: Невірна математична операція.")
        result = None

    if result is not None:
        print(f"Результат: {result}")

except ValueError:
    print("Введіть коректні числа.")

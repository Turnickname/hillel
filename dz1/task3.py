number = int(input("Enter a four-digit number: "))

digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

product = digit1 * digit2 * digit3 * digit4

print("The product of the digits is:", product)

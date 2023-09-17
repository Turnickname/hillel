num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

print("Choose an operation:")
print("1. Find maximum")
print("2. Find minimum")
print("3. Calculate average")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    maximum = max(num1, num2, num3)
    print("The maximum of the three numbers is:", maximum)
elif choice == 2:
    minimum = min(num1, num2, num3)
    print("The minimum of the three numbers is:", minimum)
elif choice == 3:
    average = (num1 + num2 + num3) / 3
    print("The average of the three numbers is:", average)
else:
    print("Invalid choice. Please select 1, 2, or 3.")

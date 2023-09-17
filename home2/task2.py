meters = float(input("Enter a length in meters: "))

print("Choose a conversion:")
print("1. Convert to miles")
print("2. Convert to inches")
print("3. Convert to yards")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    miles = meters * 0.000621371
    print(f"{meters} meters is approximately {miles} miles.")
elif choice == 2:
    inches = meters * 39.3701
    print(f"{meters} meters is approximately {inches} inches.")
elif choice == 3:
    yards = meters * 1.09361
    print(f"{meters} meters is approximately {yards} yards.")
else:
    print("Invalid choice. Please select 1, 2, or 3.")

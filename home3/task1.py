try:
    day_number = int(input("Введіть номер дня тижня (1-7): "))

    if 1 <= day_number <= 7:
        days = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }

        print(f"День тижня: {days[day_number]}")
    else:
        print("Введене число не належить діапазону від 1 до 7")
except ValueError:
    print("Введіть коректне ціле число")

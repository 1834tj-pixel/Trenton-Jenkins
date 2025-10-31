# date_calculator.py
from datetime import date, datetime, timedelta
import os

# 1. Return today's date with a given format
def today(format: str) -> str:
    try:
        return date.today().strftime(format)
    except Exception as e:
        return f"Error: Invalid date format. {e}"

# 2. Return the date plus or minus a number of days
def days_plus_or_minus(given_date: date, days: int) -> date:
    return given_date + timedelta(days=days)

# 3. Return difference between two datetimes in specific units
def date_diff(datetime1: datetime, datetime2: datetime, units: str) -> str:
    diff = datetime2 - datetime1
    seconds = diff.total_seconds()

    if units == 'seconds':
        return f"{int(seconds)} seconds"
    elif units == 'minutes':
        return f"{int(seconds // 60)} minutes"
    elif units == 'hours':
        return f"{int(seconds // 3600)} hours"
    elif units == 'days':
        return f"{diff.days} days"
    elif units == 'months':
        return f"{int(diff.days // 30)} months"
    elif units == 'years':
        return f"{int(diff.days // 365)} years"
    else:
        return "Invalid unit. Use: seconds, minutes, hours, days, months, or years."

# 4. Return the day of the week
def day_of_week(my_date: date) -> str:
    return my_date.strftime("%A")

# 5. Return a list of leap years between two dates
def leap_years_between(date1: date, date2: date) -> list:
    start, end = sorted([date1.year, date2.year])
    return [year for year in range(start + 1, end) if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))]

# 6. Return list of special days (specific weekday & day of month) between two dates
def num_of_special_days(date1: date, date2: date, day_of_week: str, day_of_month: int) -> list:
    start, end = sorted([date1, date2])
    days_list = []
    current = start
    while current <= end:
        if current.day == day_of_month and current.strftime("%A").lower() == day_of_week.lower():
            days_list.append(current.strftime("%m/%d/%Y"))
        current += timedelta(days=1)
    return days_list

# --- MAIN PROGRAM ---
def main():
    print("Welcome to the Date Calculator!")
    print("Options:")
    print("1 - Today's date (format)")
    print("2 - Add/Subtract days from a date")
    print("3 - Difference between datetimes")
    print("4 - Day of week for a date")
    print("5 - Leap years between two dates")
    print("6 - Special weekday/day-of-month occurrences\n")

    log_data = []
    while True:
        user_input = input("Enter operation and inputs (or press Enter to quit): ")
        if not user_input.strip():
            break
        log_data.append(f"> {user_input}")

        try:
            parts = user_input.split()
            op = int(parts[0])

            if op == 1:
                fmt = parts[1]
                result = today(fmt)

            elif op == 2:
                given_date = datetime.strptime(parts[1], "%m/%d/%Y").date()
                days = int(parts[2])
                result = days_plus_or_minus(given_date, days)

            elif op == 3:
                d1 = datetime.strptime(parts[1], "%m/%d/%Y")
                d2 = datetime.strptime(parts[2], "%m/%d/%Y")
                units = parts[3]
                result = date_diff(d1, d2, units)

            elif op == 4:
                d = datetime.strptime(parts[1], "%m/%d/%Y").date()
                result = day_of_week(d)

            elif op == 5:
                d1 = datetime.strptime(parts[1], "%m/%d/%Y").date()
                d2 = datetime.strptime(parts[2], "%m/%d/%Y").date()
                result = leap_years_between(d1, d2)

            elif op == 6:
                d1 = datetime.strptime(parts[1], "%m/%d/%Y").date()
                d2 = datetime.strptime(parts[2], "%m/%d/%Y").date()
                weekday = parts[3]
                day_num = int(parts[4])
                result = num_of_special_days(d1, d2, weekday, day_num)

            else:
                result = "Invalid option."

        except ValueError:
            result = "Error: Invalid date format. Please use MM/DD/YYYY."
        except Exception as e:
            result = f"Error: {e}"

        print(result)
        log_data.append(str(result))

    # --- Create log file ---
    os.makedirs("text_files", exist_ok=True)
    with open("text_files/date_calculator_logs.txt", "w") as f:
        f.write("\n".join(log_data))

    print("Log saved to text_files/date_calculator_logs.txt")
    print("Goodbye!")

# Run program
if __name__ == "__main__":
    main()

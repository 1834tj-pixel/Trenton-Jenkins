import random
from datetime import date, datetime

def example_arg(*args) -> None:
    print(args)
    a = args[0]
    b = args[1]
    b.extend([5 ,7, 3])
    print(b)

def days_plus_or_minus(given_date: date, days: int) -> date:

def date_diff(datetime1: datetime, datetime2: datetime, units: str) -> str:

def date_diff(datetime1: datetime, datetime2: datetime, units: str) -> str:

def day_of_week(my_date: date) -> str:

def leap_years_between(date1: date, date2: date) -> list

def day_of_week(my_date: date) -> str:

def leap_years_between(date1: date, date2: date) -> list:

def num_of_special_days(date1: date, date2: date, day of the week: str, day_of_month: int) -> list:

def dates_app() -> None:
    print('check out this cool dates app!')
    input_value = input('Give me some input: ')
    while len(input_value) != 0:
        try:
            input_split: list = input_value.split(' ')
            operator: str = input_split[0]
            if operator == '1':
                print(f'Today is {today(input_split[1])}')
            elif operator == '2':
                given_date: data = datetime.strptime(input_split[1], '%m/%d/%Y').date()
                days:int = int(input_split[2])
                print(days_plus_or_minus(given_date, days))
            elif operator == '3':
                datatime_1: datetime = datime.strptime(input_split[1], '%m/%d/%Y')
                datetime_2: datetime = datetime.strptime(input_split[2], '%m/%d/%Y')
            units: str = input_split[3]

           print(data_diff(datetime_1, datetime_2, units))
      elif operator == '4':
        given_date: date = datetime.strptime(input_split[1], '%m/%d/%Y')
        print(day_of_week(given_data))
     elif operator == '5':

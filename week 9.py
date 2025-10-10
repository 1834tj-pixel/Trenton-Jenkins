from datetime import datetime, data, timedelta

def main() -> None:
    tmorrow = datetime.today() + timedelta(days=-1)
    next_month = datetime.today() + timedelta(days=30)
    date1: datetime = datetime.today()
    date2: date = datetime.today()
    print(date1.strftime("%d/%m/%Y"))
    print(date2.strftime("%d/%m/%Y"))
    print(tomorrow.strftime("%d/%m/%Y"))

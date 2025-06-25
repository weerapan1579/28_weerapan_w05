from datetime import datetime, date, timedelta
import time
today = date.today()
now = datetime.now()

# จัด Format ว ด ป
formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime("%H-%M-%S")

# คำนวณวันที่
tomorow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(days=7)
next_mount = today + timedelta(days=30)

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    return age

day = int(input("Day : "))
mount = int(input("Mount : "))
year = int(input("Year : "))
birth_day = date(year,mount,day)

age = calculate_age(birth_day)
print(age)
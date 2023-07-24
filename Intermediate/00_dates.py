### dates 

# Date time

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

year_2023 = datetime(2023, 1, 1)
print(year_2023)

print(" --- " * 10) # TIME 

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print(" --- " * 10) #DATE

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 10, 6)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date( current_date.year, current_date.month + 1, current_date.day)
print(current_date)

print(" --- " * 10) ### DATE OPERATIONS

diff = now - year_2023 
print(diff)

diff = current_date -year_2023.date()
print(diff)

print(" --- " * 10) ### TIMEDELTA

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
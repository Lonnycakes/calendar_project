from utils import days_per_month
from utils import month_order
from utils import days_of_the_week

def leap_year_check(year):
    if year % 4 == 0:
        return True
    return False

DEBUG = True

assert leap_year_check(2020) == True
assert leap_year_check(2022) == False
if DEBUG:
    print("Leap year check pass!")

def create_calendar_month(month, first_day):
    # "Feb 1, Monday" : []
    month_dict = {}
    index = days_of_the_week.index(first_day)
    day_range = days_per_month[month] + 1
    for day in range(1, day_range):
        abb = month[:3]
        index %= 7
        day_of_week = days_of_the_week[index]
        key = "{} {}, {}".format(abb, day, day_of_week)
        index += 1
        month_dict.setdefault(key, [])
    return month_dict
    
FEB = create_calendar_month("February", "Friday")
assert FEB["Feb 1, Friday"] == []
assert FEB["Feb 28, Thursday"] == []
assert len(FEB) == 28
print("create_calendar_month check passed")
    
def create_calendar_year(year, first_day):
    if leap_year_check:
        pass
    calendar_year = []
    
    
    for month in month_order:
        pass
        
        
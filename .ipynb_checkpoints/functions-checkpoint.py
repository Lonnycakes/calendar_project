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
    print(month_dict)
    return month_dict

JAN = create_calendar_month("January", "Tuesday")
FEB = create_calendar_month("February", "Friday")
assert FEB["Feb 1, Friday"] == []
assert FEB["Feb 28, Thursday"] == []
assert len(FEB) == 28
print("create_calendar_month check passed")

def get_first_day(month):
    last_day = None
    for day in month:
        date = day.split(" ")
        date_num = date[1]
        date_num = date_num[0:-1]
        if int(date_num) == len(month):
            last_day = date[2]
    index = days_of_the_week.index(last_day) + 1
    index %= 7
    first_day = days_of_the_week[index]
    return first_day

assert get_first_day(FEB) == "Friday"
if DEBUG:
    print("First day check passed")

def create_calendar_year(year, first_day):
    if leap_year_check(year) == True:
        days_per_month["February"] = 29
    else:
        days_per_month["February"] = 28
    calendar_year = []
    
    for month in month_order:
        build_month = create_calendar_month(month, first_day) 
        calendar_year.append(build_month)
        
        first_day = get_first_day(build_month)
        
    return calendar_year
        
y2019 = create_calendar_year(2019, "Tuesday")
print(y2019)
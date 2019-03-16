from utils import days_per_month
from utils import month_order
from utils import days_of_the_week
from pprint import pprint

def leap_year_check(year):
    if year % 4 == 0:
        return True
    return False

DEBUG = True

assert leap_year_check(2020) == True
assert leap_year_check(2022) == False
if DEBUG:
    print("Leap year check pass!")

## This function creates "[Month] [Day], [Day of Week]" for whatever month and "first day of the month" you feed it. For example: (February, Monday) = Feb 1, Monday, Feb 2, Tuesday, etc.

def create_calendar_month(month, first_day):
    # "Feb 1, Monday" : []
    month_dict = {}
    index = days_of_the_week.index(first_day) # Gets the index of the day of the week passed by "first_day".
    day_range = days_per_month[month] + 1 # + 1 is added so the "range" includes the last day of the month (otherwise it would cut off the last day).
    for day in range(1, day_range):
        abb = month[:3]
        index %= 7
        day_of_week = days_of_the_week[index]
        key = "{} {}, {}".format(abb, day, day_of_week)
        index += 1
        month_dict.setdefault(key, [])
#     print(month_dict)
    return month_dict

JAN = create_calendar_month("January", "Tuesday")
FEB = create_calendar_month("February", "Friday")
assert FEB["Feb 1, Friday"] == []
assert FEB["Feb 28, Thursday"] == []
assert len(FEB) == 28
print("create_calendar_month check passed")

# Otherwise known as "get first day of next month". 

def get_first_day(month):
    last_day = None
    for day in month:
        date = day.split(" ")
        # Splits the value "Feb 1, Friday", for example, into list of "Feb", "1," and "Friday".
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
        # We have to update the "first_day" passed at the beginning to create every successive month as we loop through.
        first_day = get_first_day(build_month)
        
    return calendar_year
        
y2019 = create_calendar_year(2019, "Tuesday")

# for year in y2019:
#     print(year, "\n")

def parse_month(month):
    if len(month) < 3:
        month_index = int(month) - 1
    else:
        for full_name in month_order:
            if full_name.lower().startswith(month.lower()):
                month_index = month_order.index(full_name)
    return month_index

assert parse_month("May") == 4
assert parse_month("Dec") == 11
assert parse_month("December") == 11
assert parse_month("12") == 11
if DEBUG:
    print("Parse Month Check Passed!")
  
def add_task(year, time = None):
    task = input("Enter task: ") 
    month = input("Enter month: ")
    month = parse_month(month)
    date = input("Enter date: ")
    time = input ("Enter time: ")
    task = time + ": " + task
    
    for day, day_list in year[month].items():
        key = day[4:].split(",") # Example: Dec 4, 2019  ["4"," 2019"]
        if key[0] == date:
            day_list.append(task)

# Create a list of possible years from 2000 to 2031 that the user can input.
            
def create_years():
    first_day = 'Saturday'
    years = []
    for year in range(2000, 2031):
        year_list = create_calendar_year(year, first_day)
        december = year_list[11]
        first_day = get_first_day(december)
        # This sets "first_day" as the first day of the month after December, i.e. January of the next year.
        years.append(year_list)
    return years

# pprint(create_years())
from functions import create_calendar_year, add_task, parse_month, create_years
from utils import month_order

year_list = create_years()
y2019 = year_list[19]

def parse_year(year):
    index_year = int(year[2:])        
    year = year_list[index_year]
    return year

def view_calendar():
    print("View [Y]ear")
    print("View [M]onth")
    user_input = input("Please select a viewing option: ").lower()
    
    if user_input == "y":
        year_selected = input('Please enter a year: ')
        year_selected = parse_year(year_selected)
        
        for index, month in enumerate(year_selected):
            print(month_order[index], '\n', month)
        
    elif user_input == "m":
        user_month = input("Select a month: ").lower()
        month = parse_month(user_month)
        
        for day, events in y2019[month].items():
            if events != []:
                print(day, events)

def start_menu():
    print('[V]iew Calendar')
    print('[A]dd Task')
    print('[Q]uit')
    user_input = input("Choose an option: ").lower()
    
    if user_input == "v":
        print("You have selected to view calendar.")
        view_calendar()
        # We don't need to pass a specific argument because we look for user input inside the function.
        
    if user_input == "a":
        print("You have selected to add a task.")
        year = input('What year would you like to look at?')
        # If user puts in '2019':
        year = parse_year(year)
        add_task(year)
        
    if user_input == 'q':
        print('Are you sure?')
        quit_message = input('Y/N: ').lower()
        if quit_message == 'y':
            return
    
    start_menu()
    
start_menu()
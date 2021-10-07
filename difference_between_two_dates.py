from datetime import datetime

def validate_date_format(date_string):
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
         
    except ValueError:
        return False
first_string = str(input('Enter date(yyyy-mm-dd): '))
second_string = str(input('Enter date(yyyy-mm-dd): '))
date1 = validate_date_format(first_string)
date2 = validate_date_format(second_string)

if date1 == False and date2 == False:
    print("Incorrect data format, should be YYYY-MM-DD")
    print("Try again")
else:
    date_difference = date2 - date1
    print(date_difference)


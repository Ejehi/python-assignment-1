from datetime import datetime

def validate_date_format(date_string):
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
         
    except ValueError:
        return False

first_date_string = str(input('Enter date(yyyy-mm-dd):'))
second_date_string = str(input('Enter another date(yyyy-mm-dd):'))
date1 = validate_date_format(first_date_string)
date2 = validate_date_format(second_date_string)

if date1 == False and date2 == False:
    print("Incorrect data format, should be YYYY-MM-DD. Try again")
else:
    if date1 < date2:
        date_difference = date2 - date1
        print(date_difference)
    else:
        date_difference = date1 - date2
        print(date_difference)


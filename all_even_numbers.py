valid_integer_list = []

def check_if_integer(any_number):
    try:
        return int(any_number)
    except ValueError:
        return False

def collect_user_list():
    user_input = input("Please enter all the numbers you want in your list seperated by a whitespace")
    user_list = user_input.split(" ")
    for item in user_list:
        check_item = check_if_integer(item)
        valid_integer_list.append(check_item)

collect_user_list()

while False in valid_integer_list:
    print("Please enter only integer values. Try again")
    valid_integer_list.clear()
    collect_user_list()

# check to see if numbers are even
even_number_list = []
for item in valid_integer_list:
    if item % 2 == 0:
        even_number_list.append(item)

if even_number_list == []:
    print("There are no even numbers contained in your list")
else:
    print("The list below contains all even numbers in your list:")
    print(even_number_list)

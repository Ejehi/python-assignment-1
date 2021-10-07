your_list = []

def check_if_integer(any_number):
    try:
        return int(any_number)
    except ValueError:
        print('You did not enter an integer. Please try again')
        return False

def check_even_number():
    length_of_list = input("Please enter the number of integers you want in your list")

    valid_length_of_list = check_if_integer(length_of_list)

    if valid_length_of_list:

        # adding the user's list elements
        for number_input in range(valid_length_of_list):
            list_element = input("Enter an integer list item")
            valid_list_element = check_if_integer(list_element)

            while not isinstance(valid_list_element, int):
                list_element = input("Enter an integer list item")
                valid_list_element = check_if_integer(list_element)

            your_list.append(valid_list_element) 

     

        # check to see if numbers are even
        even_number_list = []
        for item in your_list:
            if item % 2 == 0:
                even_number_list.append(item)

        if even_number_list == []:
            print("There are no even numbers contained in your list")
        else:
            print("The list below contains all even numbers in your list:")
            print(even_number_list)

check_even_number()
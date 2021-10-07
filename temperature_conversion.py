def check_if_integer(any_number):
    try:
        return int(any_number)
    except ValueError:
        print('You did not enter an integer. Please try again')
        return False

print("Hello user!!!! This program converts the temperature in a given value to another (Celsius or Fahrenheit)")

your_temperature = input("Enter an integer")

valid_temperature = check_if_integer(your_temperature)

if valid_temperature:
    your_unit = input("Enter 'C' for Celscius or 'F' for fahrenheit")

    unit = your_unit.upper()


    if unit == "C":
        temperature_in_fahrenheit = float((valid_temperature * 1.8) + 32)
        print("{} in Celcius is {} in fahrenheit".format(valid_temperature, temperature_in_fahrenheit))
    elif unit == "F":
        temperature_in_celcius = float(5/9 * (valid_temperature - 32))
        print("{} in fahrenheit is {} in Celcius".format(valid_temperature, temperature_in_celcius))
    else:
        print("You did not enter 'C' or 'F' as a unit. Please try again")

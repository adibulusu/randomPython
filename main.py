# created by adi bulusu 2021

# function for actual calculations
def days_to_units(num_days, unit):
    if unit == "hours":
        return f"{num_days} days are {num_days * 24} {unit}"
    elif unit == "minutes":
        return f"{num_days} days are {num_days * 24 * 60} {unit}"
    elif unit == "seconds":
        return f"{num_days} days are {num_days * 24 * 60 * 60} {unit}"
    else:
        return "Invalid unit"

# validates if correct inputs are being given
# catch cases for invalid inputs
# executes code
def validate_and_execute():
    try:
        user_int_number = int(days_units_dict["days"])
        if user_int_number > 0:
            calculated_value = days_to_units(user_int_number, days_units_dict["unit"])
            print(calculated_value)
        elif user_int_number == 0:
            print("0 not applicable")
        else:
            print("Negative numbers not applicable")
    except ValueError:
        print("Invalid input")

# prompts user
user_input = ""
while user_input != "exit":
    user_input = input("Please enter number of days and conversion unit, colon separated \n")
    days_units = user_input.split(":")
    days_units_dict = {"days": days_units[0], "unit": days_units[1]}
    validate_and_execute()

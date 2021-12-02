def prog_one_execute(passed_dict):
    list_string = passed_dict["list"]
    ind_nums = list_string.split(",")
    # convert string list to int list
    for i in range(len(ind_nums)):
        ind_nums[i] = int(ind_nums[i])

    targ = passed_dict["target"]
    targ_int = int(targ)
    for i in range(len(ind_nums)):
        for j in range(i+1, len(ind_nums)):
            if ind_nums[i] + ind_nums[j] == targ_int:
                return [i, j]


def prog_one_start():
    user_input = input("Please enter a list of numbers and a target value, colon separated: ")
    list_and_target = user_input.split(":")
    list_and_target_dict = {"list": list_and_target[0], "target": list_and_target[1]}
    print(prog_one_execute(list_and_target_dict))


def prog_two_execute(user_input):
    to_string = str(user_input)
    rev_word = to_string[::-1]
    if rev_word == to_string:
        return "Yes, this is a palindrome"
    else:
        return "Sorry, not a palindrome"


def prog_two_start():
    user_input = input("Please enter a anything, and I will check whether it is a palindrome or not!\n")
    print(prog_two_execute(user_input))


program_value = ""
while program_value != "exit":
    print("Welcome, choose an option or type exit to close")
    program_value = input("Do you want to execute program 1 or 2\n")
    if program_value == "1":
        prog_one_start()
    elif program_value == "2":
        prog_two_start()

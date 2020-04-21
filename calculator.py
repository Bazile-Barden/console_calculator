def calculator():
    user_number = input("Enter a number....")
    if user_number.isalpha():
        print("Numbers only")

    elif user_number == "":
        calculator()

    else:
        user_operation = input("Enter an operation  ---- : ")
        # second input by user
        second_user_input = input("Enter a number again..... : ")
        if second_user_input.isnumeric():

            # Addition Operation
            if user_operation == "+":
                answer_for_addition = float(user_number) + float(second_user_input)
                print(user_number, "+", float(second_user_input), "= ", answer_for_addition)

            # Subtraction Operation
            elif user_operation == "-":
                answer_for_subtraction = float(user_number) - float(second_user_input)
                print(user_number, "-", second_user_input, "=", answer_for_subtraction)

            # Multiplication Operation
            elif user_operation == "*":
                answer_for_multiplication = float(user_number) * float(second_user_input)
                print(user_number, "*", second_user_input, "=", answer_for_multiplication)

            # division operation
            elif user_operation == "/":
                answer_for_division = float(user_number) / float(second_user_input)
                print(user_number, "/", second_user_input, "=", answer_for_division)

            elif user_operation == "":
                print("Wrong operation")

            else:
                print("wrong operation!!!!")

        else:
            print("wrong input")
        repeat()


def repeat():
    user_option = input("Do u want to continue (Y / N)----- ")

    if user_option.upper() == "Y":
        calculator()

    elif user_option.upper() == "N":
        print("DONE :) ")

    else:
        repeat()


calculator()

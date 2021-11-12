def input_save():
    while True:
        try:
            saves = int(input("Input the amount of saves you want to have: "))
            if saves <= 0:
                print("The amount of saves can't be negative: ")
                continue
            break
        except ValueError:
            print("The amount of saves must be integer value")
    return saves


def input_id():
    while True:
        try:
            number = int(input("Input ID: "))
            if number <= 0:
                print("ID can't be negative: ")
                continue
        except ValueError:
            print("ID must be integer value")
        return number


def input_value():
    value = input("Input value to change on: ")
    return value


def input_field():
    while True:
        try:
            print("Choose what you want:\n"
                  "1 - ID \n"
                  "2 - contractor_name\n"
                  "3 - contractor_email\n"
                  "4 - contractor_phone\n"
                  "5 - contractor_iban\n"
                  "6 - start_date\n"
                  "7 - due_date\n")
            what_chosen = int(input(""))
            if what_chosen == 1:
                return 'ID'
            elif what_chosen == 2:
                return 'contractor_name'
            elif what_chosen == 3:
                return 'contractor_email'
            elif what_chosen == 4:
                return 'contractor_phone'
            elif what_chosen == 5:
                return 'contractor_iban'
            elif what_chosen == 6:
                return 'start_date'
            elif what_chosen == 7:
                return 'due_date'
            else:
                print("Enter right option")
                continue
        except ValueError:
            print("Something went wrong, enter an number you want:")

import datetime
import os
from pyisemail import is_email


class Validation:

    def __init__(self):
        pass

    def check_positive(number):
        while True:
            try:
                if int(number) > 0:
                    return number
                elif int(number) <= 0:
                    print("This number can't be negative: ", number)
                    break
            except ValueError:
                print("ID must be integer!", number)
                break

    def check_name(name):
        if all(x.isalpha() or x.isspace() for x in name):
            return name
        else:
            print("Name should contain only letters: ", name)

    def check_email(email):
        check_post = is_email(email, check_dns=True)
        if check_post:
            return email
        else:
            print("Incorrect email here: ", email)

    def check_phone(phone):
        if all(x.isdigit() or x.isspace() for x in phone) and len(phone) in range(4, 11):
            return phone
        else:
            print("Phone can`t be so: ", phone)

    def check_iban(iban):
        code = iban[0:2]
        digit = iban[2:]
        if len(iban) == 29:
            if all(x.isalpha() or x.isspace() for x in code) and all(x.isdigit() or x.isspace() for x in digit):
                return iban
        else:
            print("This iban isn`t correct: ", iban)

    def check_date(date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("Incorrect date. (Year. month. day) ", date)

    def compare_dates(start_date, due_date):
        if start_date < due_date:
            return
        else:
            print(start_date, " and ", due_date, "Start date can't be bigger than due date. Try again", )

    def input_file(fl):
        while True:
            path = input(fl)
            if os.path.isfile(path) and path.endswith(".txt"):
                return path
            else:
                print("File name is incorrect. Try again")
                continue

    def check_file(path):
        if os.path.isfile(path) and path.endswith(".txt"):
            return path
        else:
            print("File can't be found")
            return Validation.input_file("Input correct file name: ")

import datetime
import os
from pyisemail import is_email


class Validation:

    def __init__(self):
        pass

    @staticmethod
    def check_name(func):
        def wrapper(self, name):
            if not all(x.isalpha() or x.isspace() for x in name):
                print("Name should contain only letters: ", name)
            func(self, name)

        return wrapper

    @staticmethod
    def check_email(func):
        def wrapper(self, email):
            if not is_email(email, check_dns=True):
                print("Incorrect email here: ", email)
            func(self, email)

        return wrapper

    @staticmethod
    def check_phone(func):
        def wrapper(self, phone):
            if not all(x.isdigit() or x.isspace() for x in phone) or len(phone) not in range(4, 11):
                print("Phone can`t be so: ", phone)
            func(self, phone)

        return wrapper

    @staticmethod
    def check_iban(func):
        def wrapper(self, iban):
            code = iban[0:2]
            digit = iban[2:]
            if not all(x.isalpha() or x.isspace() for x in code) or not all(
                    x.isdigit() or x.isspace() for x in digit) or len(iban) != 29:
                print("This iban isn`t correct: ", iban)
            func(self, iban)

        return wrapper

    @staticmethod
    def check_date(func):
        def wrapper(self, date):
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                print("Incorrect date. (Year. month. day) ", date)
            func(self, date)

        return wrapper

    @staticmethod
    def compare_dates(func):
        def wrapper(self, start_date, due_date):
            if not start_date < due_date:
                print(start_date, " and ", due_date, "Start date can't be bigger than due date. Try again")
            func(self, start_date, due_date)

        return wrapper

    def input_file(fl):
        while True:
            path = input(fl)
            if os.path.isfile(path) and path.endswith(".txt"):
                return path
            else:
                print("File name is incorrect. Try again")
                continue

    @staticmethod
    def check_file(func):
        def wrapper(self, path):
            if not os.path.isfile(path) and path.endswith(".txt"):
                print("File can't be found")
                path = Validation.input_file("Input correct file name: ")
            func(self, path)

        return wrapper

    @staticmethod
    def check_positive(func):
        def wrapper(self, number):
            if int(number) <= 0:
                print("This number can't be negative: ", number)
            func(self, number)

        return wrapper

    @staticmethod
    def check_a_contract(func):
        def wrapper(self):
            func(self)
            self.set_ID(self.get_ID())
            self.set_contractor_name(self.get_contractor_name())
            self.set_contractor_email(self.get_contractor_email())
            self.set_contractor_phone(self.get_contractor_phone())
            self.set_contractor_iban(self.get_contractor_iban())
            self.set_start_date(self.get_start_date())
            self.set_due_date(self.get_due_date())
            self.compare_dates(self.get_start_date(), self.get_due_date())

        return wrapper

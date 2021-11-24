from pyisemail import *
import datetime


class Validation:

    @staticmethod
    def check_name(func):
        def wrapper(self, name):
            if not all(x.isalpha() or x.isspace() for x in name):
                raise ValueError("Name should contain only letters: ", name)
            func(self, name)

        return wrapper

    @staticmethod
    def check_email(func):
        def wrapper(self, email):
            if not is_email(email):
                raise ValueError("Incorrect email here: ", email)
            func(self, email)

        return wrapper

    @staticmethod
    def check_iban(func):
        def wrapper(self, iban):
            code = iban[0:2]
            digit = iban[2:]
            if not all(x.isalpha() or x.isspace() for x in code) or not all(
                    x.isdigit() or x.isspace() for x in digit) or len(iban) != 29:
                raise ValueError("This iban isn`t correct: ", iban)
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
                raise ValueError(start_date, " and ", due_date, "Start date can't be bigger than due date")
            func(self, start_date, due_date)

        return wrapper

    @staticmethod
    def check_phone(func):
        def wrapper(self, phone):
            if phone[0:4] != '+380' or phone[0:4] == '+380' and len(phone) > 13 or phone[0:4] == '+380' and len(
                    phone) < 13:
                raise ValueError("Phone can`t be so: ", phone)
            func(self, phone)

        return wrapper

    @staticmethod
    def check_positive(func):
        def wrapper(self, number):
            if int(number) <= 0:
                raise ValueError("This number can't be negative: ", number)
            func(self, number)

        return wrapper

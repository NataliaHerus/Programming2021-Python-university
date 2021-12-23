from pyisemail import *
import datetime


class Validation:

    @staticmethod
    def check_name(func):
        def wrapper(self, name):
            if not all(x.isalpha() or x.isspace() for x in name):
                raise ValueError("Name should contain only letters")
            return func(self, name)

        return wrapper

    @staticmethod
    def check_email(func):
        def wrapper(self, email):
            if not is_email(email):
                raise ValueError("Incorrect email here")
            return func(self, email)

        return wrapper

    @staticmethod
    def check_iban(func):
        def wrapper(self, iban):
            code = iban[0:2]
            digit = iban[2:]
            if not all(x.isalpha() or x.isspace() for x in code) or not all(
                    x.isdigit() or x.isspace() for x in digit) or len(iban) != 29:
                raise ValueError("This iban isn`t correct")
            return func(self, iban)

        return wrapper

    @staticmethod
    def check_date(func):
        def wrapper(self, date):
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Incorrect date. (Year. month. day)")
            return func(self, date)

        return wrapper

    @staticmethod
    def compare_dates(func):
        def wrapper(contract, date2):
            if contract.start_date > date2:
                raise ValueError("Start date can't be bigger than end date")
            func(contract, date2)

        return wrapper

    @staticmethod
    def check_phone(func):
        def wrapper(self, phone):
            if phone[0:4] != '+380' or phone[0:4] == '+380' and len(phone) != 13:
                raise ValueError("Phone can't be so")
            return func(self, phone)

        return wrapper

    @staticmethod
    def check_positive(func):
        def wrapper(self, number):
            try:
                if int(number) <= 0:
                    raise ValueError("This number can't be negative")
            except ValueError:
                raise ValueError("This number can't be negative")
            return func(self, number)

        return wrapper

    @staticmethod
    def validate_amount(func):
        def wrapper(c, amount):
            if amount < 0:
                raise ValueError("There's no contracts yet that you can negotiate")
            return func(c, amount)

        return wrapper

    @staticmethod
    def validate_admin(role):
        if role != 'admin':
            raise ValueError('This action can do only admins')

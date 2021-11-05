import datetime
import os
import enum
from Date import *


class Validation:

    @staticmethod
    def check_name(func):
        def wrapper(self, name):
            if not all(x.isalpha() or x.isspace() for x in name):
                print("Name should contain only letters: ", name)
            func(self, name)

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
    def validate_date(func):
        def wrapper(emp, date):
            try:
                year, month, day = date.split("-")
                date = Date(year, month, day)
            except ValueError:
                raise ValueError("Incorrect date format.")
            return func(emp, date)

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
    def check_budget(func):
        def wrapper(self, number):
            a = number.split('.')
            if float(number) <= 0 or len(a[1]) != 2:
                print("This number can't be so: ", number)
            func(self, number)

        return wrapper


    @staticmethod
    def compare_dates(func):
        def wrapper(self, start_date, end_date):
            if not start_date < end_date:
                print(start_date, " and ", end_date, "Start date can't be bigger than due date")
            func(self, start_date, end_date)

        return wrapper

    @staticmethod
    def check_city(func):
        def wrapper(self, city):
            a = ["Rome", "Paris", "Naples", "Vienna"]
            for city in enumerate(a):
                print("Cities should contain only these: ", city)
            func(self, city)

        return wrapper

    @staticmethod
    def check_journey(func):
        def wrapper(self):
            func(self)
            self.set_city(self.get_city())
            self.set_name(self.get_name())
            self.set_budget(self.get_budget())
            self.set_start_date(self.get_start_date())
            self.set_end_date(self.get_end_date())
            self.compare_dates(self.get_start_date(), self.get_end_date())

        return wrapper

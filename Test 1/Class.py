from Date import *
from Validation import *


class Journey(object):

    def __init__(self, **kwargs):
        for (cont, default) in kwargs.items():
            setattr(self, cont, kwargs.get(cont, default))

    def __str__(self):
        string = ""
        for key, data in vars(self).items():
            string += str(key) + ": " + str(data) + "\n"
        return string

    def get_city(self):
        return self.city

    def get_budget(self):
        return self.budget

    def get_name(self):
        return self.name

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    @Validation.check_city
    def set_city(self, value):
        self.city = value

    @Validation.check_budget
    def set_budget(self, value):
        self.budget = value

    @Validation.check_name
    def set_name(self, value):
        self.name = value

    @Validation.check_date
    def set_start_date(self, value):
        self.start_date = value

    @Validation.check_date
    def set_end_date(self, value):
        self.end_date = value

    def input_product(*args):
        d = dict((cont, input(cont + ": ")) for cont in args)
        return d

    @Validation.compare_dates
    def compare_dates(self, start_date, end_date):
        return self

    @Validation.check_journey
    def validate_car_reservation(self):
        #Validation.check_city(self.set_city)
        Validation.check_name(self.set_name)
        Validation.check_budget(self.set_budget)
        Validation.check_date(self.set_start_date)
        Validation.check_date(self.set_end_date)
        Validation.compare_dates(self.compare_dates(self.start_date, self.end_date))


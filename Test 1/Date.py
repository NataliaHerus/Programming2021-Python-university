from Date_Validation import *
from datetime import date


class Date(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @property
    def day(self):
        return self._day

    @day.setter
    @ValidationDate.validate_date
    def day(self, value):
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    @ValidationDate.validate_month
    def month(self, value):
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    @ValidationDate.validate_year
    def year(self, value):
        self._year = value

    def bigger(self, date):
        if self.year > date.year:
            return True
        elif self.year == date.year:
            if self.month > date.month:
                return True
            elif self.month == date.month:
                if self.day > date.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __get_dictionary(self):
        return dict((name, getattr(self, name)) for name in dir(self) if not name.startswith('__')
                    and not name.startswith('_') and name != "input_product")

    def __str__(self):
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day)

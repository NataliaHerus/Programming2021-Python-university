from Validation import *


class Contract(object):

    def __init__(self, **kwargs):
        for (prop, default) in kwargs.items():
            setattr(self, prop, kwargs.get(prop, default))

    @property
    def name(self):
        return self.name

    @name.setter
    @Validation.check_name
    def name(self, value):
        self.name = value

    @property
    def email(self):
        return self.email

    @email.setter
    @Validation.check_email
    def email(self, value):
        self.email = value

    @property
    def phone(self):
        return self.phone

    @phone.setter
    @Validation.check_phone
    def phone(self, value):
        self.phone = value

    @property
    def iban(self):
        return self.iban

    @iban.setter
    @Validation.check_iban
    def iban(self, value):
        self.iban = value

    @property
    def start_date(self):
        return self.start_date

    @start_date.setter
    @Validation.check_date
    def start_date(self, value):
        self.start_date = value

    @property
    def end_date(self):
        return self.end_date

    @end_date.setter
    @Validation.check_date
    def end_date(self, value):
        self.end_date = value

    def __get_dictionary__(self):
        return dict((name, getattr(self, name)) for name in dir(self) if not name.startswith('__')
                    and not name.startswith('_') and name != "input_product")

    @staticmethod
    def input_product(*args):
        d = dict((prop, input(prop + " : ")) for prop in args)
        return d

    def __str__(self):
        return "Contract:\n" + '\n'.join("%s : %r" % (key2, str(val2)) for (key2, val2)
                                         in self.__get_dictionary__().items()) + "\n"

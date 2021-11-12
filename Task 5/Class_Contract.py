from Validation import *


class Contract:

    def __init__(self, **kwargs):
        for (cont, default) in kwargs.items():
            setattr(self, cont, kwargs.get(cont, default))

    def __str__(self):
        string = ""
        for key, data in vars(self).items():
            string += str(key) + ": " + str(data) + "\n"
        return string

    def get_ID(self):
        return self.ID

    def get_contractor_name(self):
        return self.contractor_name

    def get_contractor_email(self):
        return self.contractor_email

    def get_contractor_phone(self):
        return self.contractor_phone

    def get_contractor_iban(self):
        return self.contractor_iban

    def get_start_date(self):
        return self.start_date

    def get_due_date(self):
        return self.due_date

    @Validation.check_positive
    def set_ID(self, value):
        self.ID = value

    @Validation.check_name
    def set_contractor_name(self, value):
        self.contractor_name = value

    @Validation.check_email
    def set_contractor_email(self, value):
        self.contractor_email = value

    @Validation.check_phone
    def set_contractor_phone(self, value):
        self.contractor_phone = value

    @Validation.check_iban
    def set_contractor_iban(self, value):
        self.contractor_iban = value

    @Validation.check_date
    def set_start_date(self, value):
        self.start_date = value

    @Validation.check_date
    def set_due_date(self, value):
        self.due_date = value

    def input_product(*args):
        d = dict((cont, input(cont + ": ")) for cont in args)
        return d

    @Validation.compare_dates
    def compare_dates(self, start_date, due_date):
        return self

    @Validation.check_a_contract
    def validate_contract(self):
        Validation.check_positive(self.set_ID)
        Validation.check_name(self.set_contractor_name)
        Validation.check_email(self.set_contractor_email)
        Validation.check_phone(self.set_contractor_phone)
        Validation.check_iban(self.set_contractor_iban)
        Validation.check_date(self.set_start_date)
        Validation.check_date(self.set_due_date)
        Validation.compare_dates(self.compare_dates(self.start_date, self.due_date))

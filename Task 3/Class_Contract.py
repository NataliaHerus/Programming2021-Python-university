from Validation import *


class Contract:

    def __init__(self, **args):
        for (cont, default) in args.items():
            setattr(self, cont, args.get(cont, default))

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

    def set_ID(self, value):
        self.ID = value

    def set_contractor_name(self, value):
        self.contractor_name = value

    def set_contractor_email(self, value):
        self.contractor_email = value

    def set_contractor_phone(self, value):
        self.contractor_phone = value

    def set_contractor_iban(self, value):
        self.contractor_iban = value

    def set_start_date(self, value):
        self.start_date = value

    def set_due_date(self, value):
        self.due_date = value

    def input_product(*args):
        d = dict((cont, input(cont + ": ")) for cont in args)
        return d

    def validate_contract(self):
        Validation.check_positive(self.ID)
        Validation.check_name(self.contractor_name)
        Validation.check_email(self.contractor_email)
        Validation.check_phone(self.contractor_phone)
        Validation.check_iban(self.contractor_iban)
        Validation.check_date(self.start_date)
        Validation.check_date(self.due_date)
        Validation.compare_dates(self.start_date, self.due_date)


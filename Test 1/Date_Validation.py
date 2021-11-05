from calendar import monthrange


class ValidationDate:

    @staticmethod
    def validate_date(func):
        def wrapper (date, day):
            try:
                if int(day) > monthrange(date.year, date.month)[1]:
                    raise ValueError("Incorrect month.")
            except ValueError:
                raise ValueError("Incorrect day.")
            return func(date, int(day))
        return wrapper

    @staticmethod
    def validate_month(func):
        def wrapper(date, month):
            try:
                if int(month) < 1 or int(month) > 12:
                    raise ValueError("Incorrect month.")
            except ValueError:
                raise ValueError("Incorrect month.")
            return func(date, int(month))
        return wrapper

    @staticmethod
    def validate_year(func):
        def wrapper (date, year):
            try:
                if int(year) < 2020:
                    raise ValueError("Incorrect Year.")
            except ValueError:
                raise ValueError("Incorrect Year.")
            return func(date, int(year))
        return wrapper

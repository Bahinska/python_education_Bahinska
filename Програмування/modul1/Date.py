from datetime import date
from Validation import *
from Booking import *


class Date:

    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    @property
    def day(self):
        return self._day

    @day.setter
    @Validation.validateDay
    def day(self, value):
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    @Validation.validateMonth
    def month(self, value):
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    @Validation.validateYear
    def year(self, value):
        self._year = value


    def __gt__(self, other):
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
        return str(self.day) + "-" + str(self.month) + "-" + str(self.year)

    @staticmethod
    def validateDate(func):
        def validateDateWrapper(obj, date):
            try:
                day, month, year = date.split("-")
                date = Date(day, month, year)
            except ValueError:
                raise ValueError("Incorrect date format.")
            return func(obj, date)
        return validateDateWrapper
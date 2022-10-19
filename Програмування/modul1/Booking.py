from Validation import Validation
from datetime import date
from Date import *

class Booking:
    def __init__(self, **kwargs):
        er = ""
        for (prop, default) in kwargs.items():
            try:
                setattr(self, prop, default)
            except ValueError as e:
                er += "\n ~ " + str(e)
        if len(er) > 0:
            raise ValueError("Element can't be created" + er)

    def __get_dictionary(self):
        return dict((name, getattr(self, name)) for name in self.__dict__ if not name.startswith('u'))

    def __str__(self):
        return "Booking:\n" + '\n'.join("%s : %r" % (key2[1:], str(val2)) for (key2, val2)
                                            in self.__get_dictionary().items()) + "\n\n"


    @property
    def name(self):
        return self._name

    @name.setter
    @Validation.name_validation
    def name(self, n):
        self._name = n

    @property
    def pricePerDay(self):
        return self._pricePerDay

    @pricePerDay.setter
    @Validation.price_validation
    def pricePerDay(self, p):
        self._pricePerDay = p

    @property
    def startDate(self):
        return self._startDate

    @startDate.setter
    @Validation.validateDate
    def startDate(self, data):
        self._startDate = data

    @property
    def endDate(self):
        return self._endDate


    @endDate.setter
    @Date.validateDate
    def endDate(self, data):
        if data > self.startDate:
            self._endDate = data
        else:
            raise ValueError("Incorrect end date!")

    def DaysCount(self):
        f_date = date(self.startDate.year, self.startDate.month, self.startDate.day)
        s_date = date(self.endDate.year, self.endDate.month, self.endDate.day)
        delta = s_date - f_date
        return int(delta.days)
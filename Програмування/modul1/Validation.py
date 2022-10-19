import re
from calendar import *
from datetime import *

class Validation:
    @staticmethod
    def name_validation(func):
        def validate_name_Wrapper(obj, name):
            regex = "[A-Z][A-Za-z]{2,25}(\s[A-Z][A-Za-z]{2,25})?$"
            if not re.match(regex, name):
                raise ValueError("It's not proper name.")
            return func(obj, name)
        return validate_name_Wrapper

    @staticmethod
    def price_validation(func):
        def price_validation_Wrapper(obj, num):
            try:
                a = float(num)
            except:
                raise ValueError("Price must be positive float or int and must have two digits after coma!")
            if a <= 0:
                raise ValueError("Price must be positive float or int and must have two digits after coma!")
            if not re.match('[0-9]*(\.[0-9]{2})?$', num):
                raise ValueError("Price must have two digits after coma.")
            return func(obj, num)
        return price_validation_Wrapper



    @staticmethod
    def validateDay(func):
        def validateDayWrapper(date, day):
            try:
                if int(day) > monthrange(date.year, date.month)[1]:
                    raise ValueError("Incorrect month.")
                if date.year == 2019 and date.month < 10:
                    raise ValueError("Incorrect date.")
                if date.year == 2019 and date.month == 10 and int(day) < 23:
                    raise ValueError("Incorrect date.")
                if date.year < 2019:
                    raise ValueError("Incorrect date.")
            except ValueError:
                raise ValueError("Incorrect day.")
            return func(date, int(day))
        return validateDayWrapper

    @staticmethod
    def validateMonth(func):
        def validateMonthWrapper(date, month):
            try:
                if int(month) < 1 or int(month) > 12:
                    raise ValueError("Incorrect month.")
            except ValueError:
                raise ValueError("Incorrect month.")
            return func(date, int(month))
        return validateMonthWrapper

    @staticmethod
    def validateYear(func):
        def validateYearWrapper(date, year):
            try:
                if int(year) < 2015:
                    raise ValueError("Incorrect Year.")
            except ValueError:
                raise ValueError("Incorrect Year.")
            return func(date, int(year))
        return validateYearWrapper

    @staticmethod
    def biggerDate(func):
        def biggerDateWrapper(date, year):
            try:
                if int(year) < 2015:
                    raise ValueError("Incorrect Year.")
            except ValueError:
                raise ValueError("Incorrect Year.")
            return func(date, int(year))
        return biggerDateWrapper

    @staticmethod
    def validateFileName(end="json"):
        def validateFileNameDecorator(func):
            def validateFileNameWrapper(L, filename):
                if not str(filename).endswith(end):
                    raise ValueError("Incorrect filename, should end with ." + end + ".")
                return func(L, filename)
            return validateFileNameWrapper
        return validateFileNameDecorator

    @staticmethod
    def validate_inp(func):
        def validate_inpWrapper(*l):
            res = None
            while True:
                try:
                    res = func(*l)
                    break
                except ValueError as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except Exception as e:
                    print(e)
                    print("Try one more time!")
                    continue
            return res
        return validate_inpWrapper

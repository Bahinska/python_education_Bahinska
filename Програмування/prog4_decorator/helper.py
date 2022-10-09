import re
from datetime import *
import os.path

class Valid:

    @staticmethod
    def validate_id(func):
        def validate_id_Wrapper(product, value):
            regex = "^[0-9]{9}$"
            if not re.match(regex, value):
                raise ValueError("It's not proper id.")
            return func(product, value)
        return validate_id_Wrapper

    @staticmethod
    def name_validation(func):
        def validate_name_Wrapper(product, name):
            regex = "[A-Z][A-Za-z]{2,25}(\s[A-Z][A-Za-z]{2,25})?$"
            if not re.match(regex, name):
                raise ValueError("It's not proper name.")
            return func(product, name)
        return validate_name_Wrapper

    @staticmethod
    def url_validation(func):
        def url_validation_Wrapper(product, url):
            regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
            if not re.match(regex, url):
                raise ValueError("It's not proper url.")
            return func(product, url)
        return url_validation_Wrapper

    @staticmethod
    def price_validation(func):
        def price_validation_Wrapper(product, num):
            try:
                a = float(num)
            except:
                raise ValueError("Price must be positive float or int and must have two digits after coma!")
            if a <= 0:
                raise ValueError("Price must be positive float or int and must have two digits after coma!")
            if not re.match('[0-9]*(\.[0-9]{2})?$', num):
                raise ValueError("Price must have two digits after coma.")
            return func(product, num)
        return price_validation_Wrapper

    @staticmethod
    def date_validation(func):
        def date_validation_Wrapper(product, date):
            regex = "(?:0[1-9]|[12][0-9]|3[01])[-](?:0[1-9]|1[012])[-](?:19\d{2}|20[01][0-9]|20[2][0-2])"
            if not re.match(regex, date):
                raise ValueError("It's not date.")
            date_ob = datetime.strptime(date, '%d-%m-%Y')
            return func(product, date_ob)
        return date_validation_Wrapper


    @staticmethod
    def isBiggerDate(func):
        def isBiggerDate_Wrapper(product, date2):
            if hasattr(product, "_created_at"):
                if product.created_at > date2:
                    raise ValueError("Incorrect data, created_at must be lover than updated_at.")
            return func(product, date2)
        return isBiggerDate_Wrapper

    @staticmethod
    def isLessDate(func):
        def isLessDate_Wrapper(product, date2):
            if hasattr(product, "_updated_at"):
                if product.updated_at < date2:
                    raise ValueError("Incorrect data, created_at must be lover than updated_at.")
            return func(product, date2)
        return isLessDate_Wrapper

    @staticmethod
    def validateFileName(end="txt"):
        def validateFileNameDecorator(func):
            def validateFileNameWrapper(L, filename):
                if not str(filename).endswith(end):
                    raise ValueError("Incorrect filename, should end with ." + end + ".")
                return func(L, filename)
            return validateFileNameWrapper
        return validateFileNameDecorator

    @staticmethod
    def validate_inp(func):
        def validate_inpWrapper(m):
            res = None
            while True:
                try:
                    res = func(m)
                    break
                except ValueError as e:
                    print(e)
                    print("Try one more time!")
                    continue
            return res
        return validate_inpWrapper

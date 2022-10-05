import re
from datetime import *
import os.path

class Valid:
    @staticmethod
    def id_validation(ID):
        regex = "^[0-9]{9}$"
        if re.match(regex, ID):
            return ID
        else:
            raise ValueError("It's not proper id.")

    @staticmethod
    def name_validation(name):
        regex = "[A-Z][A-Za-z]{2,25}(\s[A-Z][A-Za-z]{2,25})?$"
        if re.match(regex, name):
            return name
        else:
            raise ValueError("It's not proper name.")

    @staticmethod
    def url_validation(url):
        regex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
        if re.match(regex, url):
            return url
        else:
            raise ValueError("It's not proper url.")

    @staticmethod
    def positive_float(num):
        try:
            a = float(num)
        except:
            raise ValueError("It's not proper input.")
        if a <= 0:
            raise ValueError("It's not proper input.")
        else:
            return a

    @staticmethod
    def date_validation(d):
        regex = "(?:0[1-9]|[12][0-9]|3[01])[-](?:0[1-9]|1[012])[-](?:19\d{2}|20[01][0-9]|20[2][0-2])"
        if re.match(regex, d):
             d1, m1, y1 = d.split('-')
             return date(int(y1), int(m1), int(d1))
        else:
            raise ValueError("It's not date.")

    @staticmethod
    def FileName_validation(filename, end="txt"):
        if not filename.endswith(end):
            raise ValueError("Incorrect filename, should end with ." + end + ".")
        return filename

    @staticmethod
    def file_exist(file):
        if os.path.exists(file):
            return True
        else:
            return False

    @staticmethod
    def validate_inp(func, m):
        while True:
            try:
                func(m)
                break
            except ValueError as e:
                print(e)
                print("Try one more time!")
                continue

    @staticmethod
    def compere_dates(less, more):
        if less > more:
            raise ValueError("Incorrect date!")

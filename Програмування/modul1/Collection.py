from Validation import *
import json
from Booking import *

class Collection:
    def __init__(self, *lst):
        self.id_list = []
        self.lst = list(lst[:])

    def __str__(self):
        result = ""
        for item in self.lst:
            result += str(item)
        return result

    def __getitem__(self, item):
        return self.lst[item]

    @Validation.validateFileName("json")
    def read_json_file(self, file_name):
        f = open(file_name, encoding='utf-8')
        file = json.load(f)
        for i, booking in enumerate(file):
            try:
                self.lst.append(Booking(**booking))
            except ValueError as e:
                print(str(e))
                continue
        f.close()
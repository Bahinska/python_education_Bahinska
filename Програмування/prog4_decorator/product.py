from helper import *


class Product(object):

    def __init__(self, **kwargs):
        er = ""
        for (prop, default) in kwargs.items():
            try:
                setattr(self, prop, default)
            except ValueError as e:
                er += "\n -- " + str(e)
        if len(er) > 0:
            raise ValueError("Element can't be created" + er)


    @property
    def title(self):
        return self._title

    @title.setter
    @Valid.name_validation
    def title(self, t):
        self._title = t

    @property
    def id(self):
        return self._id

    @id.setter
    @Valid.validate_id
    def id(self, ID):
        self._id = ID

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    @Valid.url_validation
    def image_url(self, url):
        self._image_url = url

    @property
    def price(self):
        return self._price

    @price.setter
    @Valid.price_validation
    def price(self, p):
        self._price = p

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    @Valid.date_validation
    @Valid.isLessDate
    def created_at(self, data):
        self._created_at = data

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    @Valid.date_validation
    @Valid.isBiggerDate
    def updated_at(self, data):
        self._updated_at = data

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, des):
        self._description = des

    def search_in_prod(self, found_string):
        result = False
        for key, value in self.__get_dictionary().items():
            if key == "created_at" or key == "updated_at":
                value = value.strftime('%d-%m-%Y')

            if found_string in str(value).lower():
                result = True
            else:
                continue
        return result

    @staticmethod
    def input_product(*args):
        d = dict((prop, input(prop + " : ")) for prop in args)
        return d

    @staticmethod
    def edit_product(el_to_edit, parameter):
        new = input(f"Enter new {parameter}: ")
        setattr(el_to_edit, parameter, new)

    def __get_dictionary(self):
        return dict((name, getattr(self, name)) for name in self.__dict__ if not name.startswith('u'))

    def __str__(self):
        return "Product:\n" + '\n'.join("%s : %r" % (key2[1:], str(val2)) for (key2, val2)
                                            in self.__get_dictionary().items()) + "\n\n"

    def dict_to_json(self):
        return dict((name[1:], getattr(self, name)) for name in self.__dict__ if not name.startswith('u'))
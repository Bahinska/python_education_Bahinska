from helper import *


class Product(object):

    def __init__(self, **kwargs):
        for (prop, default) in kwargs.items():
            setattr(self, prop, kwargs.get(prop))
        if kwargs.__len__() != 0:
            self.check_proper_prod()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, t):
        self._title = Valid.name_validation(t)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, ID):
        self._id = Valid.id_validation(ID)

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, url):
        self._image_url = Valid.url_validation(url)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, p):
        self._price = Valid.positive_float(p)

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, data):
        self._created_at = Valid.date_validation(data)

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, data):
        self._updated_at = Valid.date_validation(data)

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
    def input_product():
        prod = Product()
        prod.id = input("id : ")
        prod.title = input("title : ")
        prod.price = input("price : ")
        prod.image_url = input("image_url : ")
        prod.created_at = input("created_at : ")
        prod.updated_at = input("updated_at : ")
        Valid.compere_dates(prod.created_at, prod.updated_at)
        prod.description = input("description : ")
        return prod

    @staticmethod
    def edit_product(el_to_edit, parameter):
        new = input(f"Enter new {parameter}: ")
        setattr(el_to_edit, parameter, new)
        Valid.compere_dates(el_to_edit.created_at, el_to_edit.updated_at)

    def __get_dictionary(self):
        return dict((name, getattr(self, name)) for name in self.__dict__ if not name.startswith('u'))

    def __str__(self):
        return "Product:\n" + '\n'.join("%s : %r" % (key2[1:], str(val2)) for (key2, val2)
                                            in self.__get_dictionary().items()) + "\n\n"

    def check_proper_prod(self):
        self._id = Valid.id_validation(self._id)
        self._title = Valid.name_validation(self._title)
        self._image_url = Valid.url_validation(self._image_url)
        self._price = Valid.positive_float(self._price)
        if not isinstance(self._created_at, date) or not isinstance(self._updated_at, date):
            self._created_at = Valid.date_validation(self._created_at)
            self._updated_at = Valid.date_validation(self._updated_at)
            Valid.compere_dates(self._created_at, self._updated_at)

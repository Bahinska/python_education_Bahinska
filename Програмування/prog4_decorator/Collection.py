from product import *
import json
import uuid


class Collection:

    def __init__(self, *lst):
        self.id_list = []
        self.lst = list(lst[:])

    def __getitem__(self, item):
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __len__(self):
        return self.lst.__len__()

    def __str__(self):
        result = ""
        for item in self.lst:
            result += str(item)
        return result

    def append(self, el):
        if el.id not in self.id_list:
            self.lst.append(el)
            self.id_list.append(el.id)
        else:
            raise ValueError("Two elements with same id cannot exist!")

    @Valid.validate_id
    def delete(self, id):
        for item in self.lst:
            if str(item.id) == id:
                self.lst.remove(item)
                self.id_list.remove(item.id)
                break
        else:
            raise ValueError('No product with such ID found')

    @Valid.validate_id
    def get_by_id(self, search_id):
        found = False
        for item in self.lst:
            if item.id == search_id:
                found = True
                return item
        if not found:
            raise ValueError("No elements with such id")

    def edit(self, el_to_edit, parameter):
        if parameter == "id":
            new_id = (input("New id : "))
            if new_id in self.id_list:
                raise ValueError("Mistake! Value with this id already exist")
            else:
                old_id = el_to_edit.id
                el_to_edit.id = new_id
                self.id_list.remove(old_id)
                self.id_list.append(new_id)
        else:
            Product.edit_product(el_to_edit, parameter)

    def __edit_id(self, el_to_edit, new_id):
        if new_id in self.id_list:
            raise ValueError("Mistake! Value with this id already exist")
        else:
           self.id_list.remove(el_to_edit.id)
           self.id_list.append(new_id)
           el_to_edit.id = new_id

    def search(self, found_string):
        found_string = found_string.lower()
        founds = Collection()
        for item in self.lst:
            if item.search_in_prod(found_string):
                founds.append(item)
        return founds

    def sort(self, field="title"):
        if field == 'price':
            self.lst = sorted(self.lst, key=lambda product: float(getattr(product, field)))
        else:
            self.lst = sorted(self.lst, key=lambda product: str(getattr(product, field)).lower())

    @Valid.validateFileName("txt")
    def write_in_txt(self, file_name, mode="w"):
        f = open(file_name, mode=mode, encoding="utf-8")
        f.writelines(str(i) + "\n" for i in self.lst)
        f.close()

    @Valid.validateFileName("json")
    def write_in_json(self, file_name):
        temp = []
        with open(file_name, 'w', encoding='utf-8') as outfile:
            for ob in self.lst:
                dictionary = ob.dict_to_json()
                dictionary["created_at"] = dictionary["created_at"].strftime('%d-%m-%Y')
                dictionary["updated_at"] = dictionary["updated_at"].strftime('%d-%m-%Y')
                temp.append(dictionary)
            json.dump(temp, outfile, ensure_ascii=False)
        outfile.close()

    @Valid.validateFileName("json")
    def read_json_file(self, file_name):
        f = open(file_name, encoding='utf-8')
        file = json.load(f)
        for i, product in enumerate(file):
            try:
                if product["id"] not in self.id_list:
                    self.lst.append(Product(**product))
                    self.id_list.append(product["id"])
            except ValueError as e:
                print(str(e))
                continue
        f.close()

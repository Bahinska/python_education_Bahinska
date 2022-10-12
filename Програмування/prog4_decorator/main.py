from Collection import *
from helper import *

def menu():
    collection = Collection()
    while True:
        help_message = get_help_message()
        task = input(help_message)
        if task == '1':
            read_json(collection)
        if task == '2':
            sort(collection)
        if task == '3':
            search(collection)
        if task == '4':
            add(collection)
        if task == '5':
            delete(collection)
        if task == '6':
            edit(collection)
        if task == '7':
            write_in_txt(collection)
        if task == '8':
            write_in_json(collection)
        if task == '9':
            add_to_jsonFile(collection)
        if task == '10':
            del_from_jsonFile(collection)
        if task == '11':
            print(collection)
        if task == 'exit':
            quit()


def get_help_message():
    help_message = "*" * 51
    help_message += "\n  HELP:" + 42 * " " + "\n  Possible commands:" + 29 * " " + \
                    "\n  1  - to read from file. " + 25 * " " + \
                    "\n  2  - to sort elements. " + 25 * " " + \
                    "\n  3  - to search element.  " + 20 * " " + \
                    "\n  4  - to add Product to collection. " + 10 * " " + \
                    "\n  5  - to del Product from collection.  " + 10 * " " + \
                    "\n  6  - to edit Product in collection.  " + 9 * " " + \
                    "\n  7  - to write collection elements to txt file.  " \
                    "\n  8  - to write collection elements to json file. " \
                    "\n  9  - add product to json file. " + \
                    "\n  10 - delete product from json file. " + \
                    "\n  11 - to print collection. " + 22 * " " + \
                    "\n  exit - to exit.  " + 30 * " " + "\n"
    help_message += "*" * 51 + "\n"
    return help_message


@Valid.validate_inp
def read_json(collection):
    file = input("File name: ")
    if os.path.exists(file):
        collection.read_json_file(file)
        return file
    else:
        raise ValueError("File does not exist!")

@Valid.validate_inp
def sort(collection):
    possible = ['title', 'image_url', 'price', 'created_at', 'updated_at', 'description', 'id']
    string = input("Enter field for which you want to sort: \n"
                 "POSSIBLE: id, title, image_url, price, created_at, updated_at, description:\n")
    if string not in possible:
        raise ValueError("Incorrect sort request")
    else:
        collection.sort(string)

@Valid.validate_inp
def search(collection):
    request = input("Search query: ")
    result = collection.search(request)
    if len(result) > 0:
        print("Results of search:\n")
        print(result)
    else:
        print("Nothing was found :(")

@Valid.validate_inp
def add(collection):
    d = Product.input_product("id", "title", "image_url", "price", "created_at", "updated_at", "description")
    collection.append(Product(**d))
    print("Successfully added!\n")

@Valid.validate_inp
def delete(collection):
    collection.delete(input("Element to del id: "))
    print("Successfully deleted!\n")

@Valid.validate_inp
def edit(collection):
    edit_id = input("Which Product you want to edit? (input id) ")
    if edit_id not in collection.id_list:
        raise ValueError("Mistake! Value with this id does not exist")

    possible = ['title', 'image_url', 'price', 'created_at', 'updated_at', 'description', 'id']
    parameter = input("Enter field for which you want to edit: \n"
                   "POSSIBLE: id, title, image_url, price, created_at, updated_at, description:\n")
    if parameter in possible:
       el_to_edit = collection.get_by_id(edit_id)
       collection.edit(el_to_edit, parameter)
    else:
        raise ValueError("Incorrect edit request")

@Valid.validate_inp
def add_to_jsonFile(collection):
    file = read_json(collection)
    add(collection)
    collection.write_in_json(file)

@Valid.validate_inp
def del_from_jsonFile(collection):
    file = read_json(collection)
    delete(collection)
    collection.write_in_json(file)

@Valid.validate_inp
def write_in_txt(collection):
    collection.write_in_txt((input("Enter file name: ")))

@Valid.validate_inp
def write_in_json(collection):
    collection.write_in_json(input("Enter file name: "))


if __name__ == '__main__':
    menu()
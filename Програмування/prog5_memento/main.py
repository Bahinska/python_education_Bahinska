from Collection import *
from helper import *
from CareTaker import *


def menu():
    collection = Collection()
    originator = Originator()
    history = CareTaker()

    originator.article = collection.__copy__()
    history.addMemento(originator.save(), "Start")
    file = None
    while True:
        help_message = get_help_message()
        task = input(help_message)
        if task == '1':
            file = read_json(collection)
            save(collection, originator, history, "read from file")
        if task == '2':
            request = sort(collection)
            save(collection, originator, history, f"sort: {request}")
        if task == '3':
            request, collection = search(collection)
            save(collection, originator, history, f"search: {request}")
        if task == '4':
            add(collection)
            save(collection, originator, history, "add product")
        if task == '5':
            delete(collection)
            save(collection, originator, history, "delete product")
        if task == '6':
            edit(collection)
            save(collection, originator, history, "edit product")
        if task == '7':
            write_in_json(collection, file)
        if task == '8':
            print(collection)
        if task == '<':
            collection = undo(originator, history)
        if task == '>':
            collection = redo(originator, history)
        if task == "show":
            history.show_actions()
        if task == 'exit':
            quit()

        if file != None:
            collection.write_in_json(file)



def get_help_message():
    help_message = "*" * 51
    help_message += "\n  Possible commands:" + \
                    "\n  1  - to read from file. " + \
                    "\n  2  - to sort elements. " + \
                    "\n  3  - to search element.  " + \
                    "\n  4  - to add Product to collection. " + \
                    "\n  5  - to del Product from collection.  " + \
                    "\n  6  - to edit Product in collection.  " + \
                    "\n  7  - to write collection elements to json file. " \
                    "\n  8  - to print collection. " + \
                    "\n  <  - to undo. " + \
                    "\n  >  - to redo. " + \
                    "\n  show - to show history" +\
                    "\n  exit - to exit.  \n"
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
        return string

@Valid.validate_inp
def search(collection):
    request = input("Search query: ")
    result = collection.search(request)
    if len(result) > 0:
        print("Results of search:\n")
        print(result)
    else:
        print("Nothing was found :(")
    return request, result

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
def write_in_json(collection, file):
    if file == None:
        collection.write_in_json(input("Enter file name: "))
    else:
        collection.write_in_json(file)

@Valid.validate_inp
def save(collection, originator, history, action):
    to_save = copy.deepcopy(collection.__copy__())
    originator.article = to_save
    history.addMemento(originator.save(), action)


def undo(originator, history):
    originator.restore(history.undo())
    return copy.deepcopy(originator.__copy__())


def redo(originator, history):
    originator.restore(history.redo())
    return copy.deepcopy(originator.__copy__())


if __name__ == '__main__':
    menu()

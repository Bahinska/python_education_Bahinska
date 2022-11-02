import copy
from Context import *
from LinkedList import *
from Event import *
from Observer import *


def menu():
    l = LinkedList()
    context = None
    file = None
    ob = Observer()
    ob.new("Add", Logger.write_to_file)
    ob.new("Delete", Logger.write_to_file)
    ob.new("Proces", Logger.write_to_file)

    while True:
        help_message = get_help_message()
        task = input(help_message)
        if task == "1":
            context = Context(Gen_iterator())
            print("Success! Strategy first in work")
        elif task == "2":
            context = Context(From_file())
            print("Success! Strategy second in work")
        elif task == "3":
            file = generate_list(l, context, ob)
        elif task == "4":
            del_by_pos(l, ob)
        elif task == "5":
            del_between_indexes(l, ob)
        elif task == "6":
            add(l, ob)
        elif task == "7":
             method(l, ob)
        elif task == "8":
             print(l)
        elif task == "9":
            quit()
        else:
            continue
        print()


def get_help_message():
    help_message = " Possible commands:" + \
                    "\n  1 - to use strategy 1 (iterator)" + \
                    "\n  2 - to use strategy 2 (file)" + \
                    "\n  3 - to generate elements  " + \
                    "\n  4 - to delete element by position " + \
                    "\n  5 - to delete elements between positions  " + \
                    "\n  6 - to add element in position" + \
                    "\n  7 - to use list method  " + \
                    "\n  8 - to print list  " + \
                    "\n  9 - to exit  \n"
    return help_message

@Validation.validate_inp
def generate_list(l, context, ob):
    if context == None:
        print("Choose strategy first")
        return
    before_list = copy.deepcopy(l)
    file = None
    if isinstance(context.strategy, Gen_iterator):
        print("Enter n : ")
        n = Validation.input_positive_int()
        print("Enter range (reminder: [1000; 9999])")
        a, b = Validation.range_input(1000, 9999)
        if (b - a + 1) < n:
            raise ValueError("Iteration error")
        print("Input position: ")
        pos = Validation.input_pos()
        context.generate_list(l, pos, n, a, b)

    if isinstance(context.strategy, From_file):
        file = Validation.file_exist(input("Enter file: "))
        print("Input position: ")
        pos = Validation.input_pos()
        context.generate_list(l, pos, file)

    event = Event("Add", l, pos, before_list)
    event.new_event(ob)
    return file

@Validation.validate_inp
def del_by_pos(l, ob):
    if l.len() == 0:
        print("empty list")
    else:
        print("Input position: ")
        pos = Validation.input_pos()
        before = copy.deepcopy(l)
        l.delete_by_index(pos)

        event = Event("Delete", l, pos, before)
        event.new_event(ob)

@Validation.validate_inp
def del_between_indexes(l, ob):
    if l.len() == 0:
        print("empty list")
    else:
        print("from: ", end='')
        fromm = Validation.input_pos()
        print("to: ", end='')
        to = Validation.input_pos()
        low, high = Validation.LowHeight(fromm, to)
        before = copy.deepcopy(l)
        l.delete_between_pos(low, high)

        event = Event("Delete", l, (fromm, to), before)
        event.new_event(ob)

@Validation.validate_inp
def add(l, ob):
    value = Validation.number_check(input("Value = "), 1000, 9999)
    print("Input position: ")
    pos = Validation.input_pos()
    before = copy.deepcopy(l)
    l.insert(value, pos)

    event = Event("Add", l, pos, before)
    event.new_event(ob)

def method(l, ob):
    if l.len() == 0:
        print("empty list")
    else:
        before = copy.deepcopy(l)
        l.processing()

        event = Event("Proces", l, " - ", before)
        event.new_event(ob)

if __name__ == '__main__':
    menu()

from Context import *
from LinkedList import *


def menu():
    l = LinkedList()
    context = None
    while True:
        help_message = get_help_message()
        task = input(help_message)
        if task == "1":
            context = Context(Gen_iterator())
        elif task == "2":
            context = Context(From_file())
        elif task == "3":
            generate_list(l, context)
        elif task == "4":
            del_by_pos(l)
        elif task == "5":
             del_between_indexes(l)
        elif task == "6":
             method(l)
        elif task == "7":
             print(l)
        elif task == "8":
            break
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
                    "\n  6 - to use list method  " + \
                    "\n  7 - to print list  " + \
                    "\n  8 - to exit  \n"
    return help_message

@Validation.validate_inp
def generate_list(l, context):
    if context == None:
        print("choose strategy first")
        return

    if isinstance(context.strategy, Gen_iterator):
        print("Enter u : ")
        n = Validation.input_positive_int()
        print("Enter range (reminder: [1000; 9999])")
        a, b = Validation.range_input(1000, 9999)
        if (b - a + 1) < n:
            raise ValueError("Iteration error")
        pos = Validation.number_check(input("Position: "), 0, 10000)
        context.generate_list(l, pos, n, a, b)

    if isinstance(context.strategy, From_file):
        file = Validation.file_exist(input("Enter file: "))
        pos = Validation.number_check(input("Position: "), 0, 10000)
        context.generate_list(l, pos, file)

@Validation.validate_inp
def del_by_pos(l):
    if l.len() == 0:
        print("empty list")
    else:
        pos = Validation.number_check(input("Position: "), 0, 10000)
        l.delete_by_index(pos)

@Validation.validate_inp
def del_between_indexes(l):
    if l.len() == 0:
        print("empty list")
    else:
        print("from: ", end='')
        fromm = Validation.input_pos()
        print("to: ", end='')
        to = Validation.input_pos()
        low, high = Validation.LowHeight(fromm, to)
        l.delete_between_pos(low, high)

def method(l):
    if l.len() == 0:
        print("empty list")
    else:
        l.processing()

if __name__ == '__main__':
    menu()
from LinkedList import *
from Iterator import RandIterator
from Generator import randGenerator


def menu():
    while True:
        list = LinkedList()
        print(" 1 - for your list\n"
              " 2 - for random list\n"
              " 3 - for list by iterator\n"
              " 4 - for list by generator\n"
              " 5 - to exit")
        choice = input()
        if choice == '1':
            validate_inp(user_list, list)
        elif choice == '2':
            validate_inp(random_list, list)
        elif choice == '3':
            validate_inp(iterator_list, list)
        elif choice == '4':
            validate_inp(generator_list, list)
        elif choice == '5':
            exit()
        else:
            continue

def menu2(list):
    while True:
        print("\n 1 - to go to start\n"
              " 2 - to add element by index\n"
              " 3 - to delete element by index\n"
              " 4 - to processing again\n"
              " 5 - to exit")
        choice = input()
        if choice == '1':
            menu()
        elif choice == '2':
            validate_inp(add, list)
        elif choice == '3':
            validate_inp(dell, list)
        elif choice == '4':
            list.processing()
            print(list)
        elif choice == '5':
            exit()
        else:
            continue


def user_list(list):
    print("Enter the size of list")
    size = input_positive_int()
    list.user_input(size)
    print("list: ", list)
    list.processing()
    print("Result: ", list)
    menu2(list)

def random_list(list):
    print("Enter the size of array")
    size = input_positive_int()
    list.random_gen(size)
    print("list: ", list)
    list.processing()
    print("Result: ", list)
    menu2(list)

def iterator_list(list):
    print("Enter the size of array")
    size = input_positive_int()
    a, b = range_input()
    random = RandIterator(a, b)
    iterator = iter(random)
    for i in range(size):
        list.push_back(next(iterator))
    print("list: ", list)
    list.processing()
    print("Result: ", list)
    menu2(list)

def generator_list(list):
    print("Enter the size of array")
    size = input_positive_int()
    a, b = range_input()
    random = randGenerator(a, b)
    for i in range(size):
        list.push_back(next(random))
    print("list: ", list)
    list.processing()
    print("Result: ", list)
    menu2(list)

def add(list):
    value = number_check(input("Value = "))
    pos = int(input("Index = "))
    list.insert(value, pos)
    print(list)
    menu2(list)

def dell(list):
    index = int(input("Index = "))
    list.delete_by_index(index)
    print(list)
    menu2(list)


if __name__ == '__main__':
  menu()
from LinkedList import *


def menu():
    while True:
        list = LinkedList()
        print("Enter 1 for your list\nEnter 2 for random list\nEnter 3 to exit")
        choice = input()
        if choice == '1':
            print("Enter the size of list")
            size = input_positive_int()
            list.user_input(size)
            print("list: ", list)
            list.processing()
            print("Result: ", list)
            menu2(list)
        elif choice == '2':
            print("Enter the size of array")
            size = input_positive_int()
            list.random_gen(size)
            print("list: ", list)
            list.processing()
            print("Result: ", list)
            menu2(list)
        elif choice == '3':
            exit()
        else:
            continue

def menu2(list):
    while True:
        print("Enter 1 to go to start\nEnter 2 to add element by index\nEnter 3 to delete element by index\nEnter 4 to processing again\nEnter 5 to exit")
        choice = input()
        if choice == '1':
            menu()
        elif choice == '2':
            print("Value =")
            value = number_check(input())
            print("Index = ")
            pos = int(input())
            list.insert(value, pos)
            print(list)
            menu2(list)
        elif choice == '3':
            print("Index = ")
            index = input_positive_int()
            list.delete_by_index(index)
            print(list)
            menu2(list)
        elif choice == '4':
            list.processing()
            print(list)
        elif choice == '5':
            exit()
        else:
            continue

if __name__ == '__main__':
    menu()

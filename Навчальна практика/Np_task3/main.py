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
        elif choice == '2':
            print("Enter the size of array")
            size = input_positive_int()
            list.random_gen(size)
            print("list: ", list)
            list.processing()
            print("Result: ", list)
        elif choice == '3':
            exit()
        else:
            continue


if __name__ == '__main__':
    menu()
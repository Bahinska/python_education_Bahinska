# Задано N чотиризначних натуральних чисел.
# Стиснути масив, видаливши з нього всі елементи,
# які не виконують одну з умов: 1) XYXY, 2) XYYX.
# Елементи, що звільнилися в кінці масиву, заповнити нулями.

import numpy as np


def choice_validation(a):
    while True:
        try:
            a = int(a)
        except:
            print("Wrong input. Try again")
            a = input()
            continue
        if (a == 1) | (a == 2):
            return a
        else:
            print("Wrong input. Try again")
            a = input()
            continue


def size_validation(a):
    while True:
        try:
            a = int(a)
        except:
            print("Wrong input. Try again")
            a = input()
            continue
        if a < 1:
            print("Wrong input. Try again")
            a = input()
            continue
        break
    return a


def number_validation(a):
    while True:
        try:
            a = int(a)
        except:
            print("Wrong input. Try again")
            a = input()
            continue
        if (a < 1000) | (a > 9999):
            print("Numbers must be in range 999 < x < 10000")
            a = input()
            continue
        break
    return a


def processing(array):
    for i in array:
        i = str(i)
        x = i[0]
        y = i[1]
        if ((i[2] == x) & (i[3] == y)) | ((i[2] == y) & (i[3] == x)):
            continue
        else:
            array = np.delete(array, np.argwhere(array == int(i)))
            array = np.append(array, 0)
    return array


def task_with_randon(size):
    array = np.random.randint(1000, 10000, size, int)
    print("Array: ", array)
    result = processing(array)
    print("Result: ", result)


def task_with_user(size):
    print("Input nums from 1000 to 9999")
    array = np.array([], dtype=int)
    for i in range(size):
        num = number_validation(input())
        array = np.append(array, num)
    print("Array: ", array)
    result = processing(array)
    print("Result: ", result)


def menu():
    print("Enter 1 for random array\nEnter 2 for your array")
    choice = choice_validation(input())
    print("Enter the size of array")
    size = size_validation(input())
    if choice == 1:
        task_with_randon(size)
    else:
        task_with_user(size)


if __name__ == '__main__':
    menu()
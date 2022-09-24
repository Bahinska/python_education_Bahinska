def number_check(a):
    minNum = 1000
    maxNum = 9999
    while True:
        try:
            a = int(a)
        except:
            print("Wrong input. Try again")
            a = input()
            continue
        if (a < minNum) | (a > maxNum):
            print("Numbers must be in range 999 < x < 10000")
            a = input()
            continue
        break
    return a


def input_positive_int():
    while True:
        try:
            a = int(input())
        except:
            print("Must be positive integer only")
            continue
        if a < 1:
            print("Must be positive integer only")
            continue
        break
    return a


def range_input():
    a = number_check(input("a = "))
    b = number_check(input("b = "))
    while True:
        if a >= b:
            print("Wrong input (It must be range a < b). Try again")
            a = input("a = ")
            b = input("b = ")
            continue
        break
    return a, b
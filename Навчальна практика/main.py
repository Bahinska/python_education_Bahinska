#1. Користувач повинен мати 2 опції:
#ввести масив довжини N з клавіатури
#згенерувати довільний масив довжини N зі значень,
# які знаходяться в діапазоні [a, b], де a,b вводяться з клавіатури.
#    Реалізувати алгоритм mergeSort для сортування даного масиву.
#    Вивести кількість операцій, яка була необхідною для сортування масиву.
# Програма повинна закінчувати свою роботу тільки у випадку,
# коли користувач натиснув відповідний пункт меню.
import random

def size_validation(a):
    while True:
        try:
            a = int(a)
        except:
            print("Wrong input (integer only). Try again")
            a = input()
            continue
        if a < 1:
            print("Wrong input (positive only). Try again")
            a = input()
            continue
        break
    return a

def number_validation(a):
    while True:
        try:
            a = float(a)
        except:
            print("Wrong input. Try again")
            a = input()
            continue
        break
    return a


def range_validation():
    a = number_validation(input("a = "))
    b = number_validation(input("b = "))
    while True:
        if a >= b:
            print("Wrong input (It must be range a < b). Try again")
            a = number_validation(input("a = "))
            b = number_validation(input("b = "))
            continue
        break
    return a, b


def task_with_user(size):
    print("Input nums: ")
    array = []
    for i in range(size):
        num = number_validation(input())
        array.append(num)
    print("Array: ", array)
    operations, comparisons = Merge_Sort(array)
    print("Result: ", array, "\nThere were used ", comparisons, " comparison and ", operations, " operations")


def task_with_random(size):
    array = []
    print("Enter range [a, b]")
    a, b = range_validation()
    array = [random.uniform(a, b) for _ in range(size)]
    print("Array: ", array)
    operations, comparisons = Merge_Sort(array)
    print("Result: ", array, "\nThere were used ", comparisons, " comparison and ", operations, " operations")


def merge(array, temp, From, mid, to, operations, comparisons):
    a = From
    start = From
    middle = mid + 1

    operations += 3
    while start <= mid and middle <= to:
        comparisons += 2
        if array[start] < array[middle]:
            temp[a] = array[start]
            start += 1
            comparisons += 1
            operations += 2
        else:
            temp[a] = array[middle]
            middle += 1
            operations += 2
        a += 1
        operations += 1

    # remaining elements
    while start < len(array) and start <= mid:
        temp[a] = array[start]
        a += 1
        start += 1

        comparisons += 2
        operations += 3
    # copy back
    for b in range(From, to + 1):
        array[b] = temp[b]
        operations += 1


# Iterative sort
def Merge_Sort(array):
    comparisons, operations = 0, 0
    low = 0
    high = len(array) - 1
    # sort list
    temp = array.copy()
    d = 1
    
    operations += 4
    while d <= high - low:
        comparisons += 1
        for i in range(low, high, 2 * d):
            From = i
            mid = i + d - 1
            to = min(i + 2 * d - 1, high)
            operations += 3
            merge(array, temp, From, mid, to, operations, comparisons)

        d *= 2
        operations += 1

    return operations, comparisons

def menu():
    while True:
        print("Enter 1 for your array\nEnter 2 for random array\nEnter 3 to exit")
        choice = input()
        if choice == '3':
            exit()
        elif choice == '1':
            print("Enter the size of array")
            size = size_validation(input())
            task_with_user(size)
        elif choice == '2':
            print("Enter the size of array")
            size = size_validation(input())
            task_with_random(size)
        else:
            continue


if __name__ == '__main__':
    menu()
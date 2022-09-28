#Завдання повинно бути виконано з мінімальною кількістю операцій,
#використанням мінімальної кількості циклів та з використанням функцій.
#Користувач має мати право безліч разів тестувати програму.
#По закінченню тестування користувач має мати змогу вийти з меню.
#Утворити квадратну матрицю порядку  і вивести її на екран:
import numpy as np

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


def matrix(size):
    mat = np.array([[0 for col in range(size)] for row in range(size)])
    for row in range(size):
        for col in range(size):
            mat[row][col] = row * size + col + 1
    return mat


def print_matrix(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

def menu():
     while True:
            print("Enter 1 to generate matrix\nEnter 2 to exit")
            choice = input()
            if choice == '1':
                print("Enter size: ")
                size = input_positive_int()
                m = matrix(size)
                print_matrix(m)
            elif choice == '2':
                exit()
            else:
                continue

if __name__ == '__main__':
    menu()


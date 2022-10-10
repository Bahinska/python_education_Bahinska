import os.path


class Validation:
    @staticmethod
    def number_check(a, low, high):
        while True:
            try:
                a = int(a)
            except:
                print("Wrong input. Try again")
                a = input()
                continue
            if (a < low) | (a > high):
                print(f"Numbers must be in range {low} < x < {high}. Try again")
                a = input()
                continue
            break
        return a

    @staticmethod
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

    @staticmethod
    def input_pos():
        while True:
            try:
                a = int(input())
            except:
                print("Must be positive integer only")
                continue
            if a < 0:
                print("Must be positive integer only")
                continue
            break
        return a

    @staticmethod
    def range_input(low, high):
        while True:
            a = Validation.number_check(input("a = "), low, high)
            b = Validation.number_check(input("b = "), low, high)
            if a >= b:
                print("Wrong input (It must be range a < b). Try again")
                a = input("a = ")
                b = input("b = ")
                continue
            break
        return a, b

    @staticmethod
    def validate_inp(func):
        def validate_inpWrapper(*l):
            while True:
                try:
                    func(*l)
                    break
                except ValueError as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except Exception as e:
                    print(e)
                    print("Try one more time!")
                    continue
        return validate_inpWrapper

    @staticmethod
    def file_exist(filename):
        if not os.path.exists(filename):
            raise Exception("file does not exist")
        return filename

    @staticmethod
    def fourDigit(num):
        return len(num) == 4 and num.isdigit()

    @staticmethod
    def LowHeight(low, heigh):
        try:
            if low > heigh:
                raise ValueError("Low int must be lover than height.")
        except ValueError:
            raise ValueError("Low and height must be two integers.")
        return low, heigh
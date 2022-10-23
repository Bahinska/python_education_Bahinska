from LinkedList import *
from Iterator import RandIterator

class Strategy:
    @staticmethod
    def cteate_list(data : LinkedList, pos, *args ):
        pass


class Gen_iterator (Strategy):
    @staticmethod
    def cteate_list(data: LinkedList, pos, *args):  # *args = [ n, a, b ]
        random = RandIterator(args[1], args[2])  # from a to b
        iterator = iter(random)
        for i in range(args[0]):  # n
            data.insert(next(iterator), pos)
            pos += 1


class From_file (Strategy):
    @staticmethod
    def cteate_list(data: LinkedList, pos, *args):  # *args = [ "filename" ]
        with open(args[0], "r") as infile:
            for line in infile:
                for x in line.split():
                    if Validation.fourDigit(x):
                        data.insert(int(x), pos)
                        pos += 1
                    else:
                        print(x, "not a proper input")
        infile.close()
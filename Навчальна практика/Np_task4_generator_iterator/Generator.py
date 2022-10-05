from random import randint


def randGenerator(smallest=0, largest=1000):
    while True:
        yield randint(smallest, largest)
from Logger import Logger


class Observer:

    def __init__(self):
        self._list = {}

    def new(self, key, func):
        self._list[key] = func

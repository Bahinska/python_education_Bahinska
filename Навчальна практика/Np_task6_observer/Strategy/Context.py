from Strategy import *

class Context():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def generate_list(self, data, pos, *args) -> None:
        self._strategy.cteate_list(data, pos, *args)

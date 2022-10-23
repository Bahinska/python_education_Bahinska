class Memento:

    def __init__(self, st):
        self._state = st

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, st):
        self._state = st

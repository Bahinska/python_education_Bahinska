from Memento import *

class Originator:
    def __init__(self):
        self._article = None

    @property
    def article(self):
        return self._article

    @article.setter
    def article(self, ar):
        self._article = ar

    def save(self):
        return Memento(self._article)

    def restore(self, m):
        self.article = m.state

    def __copy__(self):
        art = self.article
        return art

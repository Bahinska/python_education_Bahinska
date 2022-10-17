from Memento import *
from Originator import *

class CareTaker:
    size = 5
    def __init__(self):
        self.action_history = list()
        self.history = list()
        self._currState = -1

    def addMemento(self, m, act):
        if len(self.history) == CareTaker.size:
            self.history.pop(0)
            self.action_history.pop(0)
            self._currState -= 1
        #  if add in the end
        if self._currState == len(self.history) - 1:
            self.history.append(m)
            self.action_history.append(act)
            self._currState = len(self.history) - 1
        #  if insert
        else:
            self.history.insert(self._currState + 1, m)
            self.action_history.insert(self._currState + 1, act)
            #  видалямо історію яка після повернення та останньої дії
            del self.action_history[self._currState + 2:]
            del self.history[self._currState + 2:]
            self._currState += 1

    def getMemento(self, index):
        return self.history.__getitem__(index)

    def undo(self):
        if self._currState < 0:
            print("Impossible to undo. No actions")
            return self.getMemento(0)
        if self._currState == 0:
            print("Impossible to undo. No actions before")
            return self.getMemento(0)
        else:
            print("Undo done!")
            self._currState -= 1
            return self.getMemento(self._currState)

    def redo(self):
        if self._currState >= len(self.history) - 1:
            print("Impossible to redo. No actions next")
            self._currState = len(self.history) - 1
            return self.getMemento(self._currState)
        else:
            print("Redo done!")
            self._currState += 1
            return self.getMemento(self._currState)

    def show_actions(self):
        if self._currState == -1 :
            print("Empty history")
            return
        for i, act in enumerate(self.action_history):
            print(f"{i+1}. {act}")
        print(f"current: {self._currState + 1}")

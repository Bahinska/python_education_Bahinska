from Observer import Observer

class Event:
    def __init__(self, name, changed, posOrRange, before):
        self.name = name
        self.changed = changed
        self.posOrRange = posOrRange
        self.before = before

    def new_event(self, ob):
        if self.name in ob._list:
            ob._list[self.name](self)

    def __str__(self):
        return f"{self.name}. New list: [{self.changed}], by/on position {self.posOrRange}, Previous list: [{self.before}]"


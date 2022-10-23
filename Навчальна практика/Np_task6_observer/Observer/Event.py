from Observer import Observer

class Event:
    def __init__(self, name, changed, posOrRange, before, log=True):
        self.name = name
        self.changed = changed
        self.posOrRange = posOrRange
        self.before = before

        if log:
            self.log_event()

    def log_event(self):
        for observer in Observer._observers:
            if self.name in observer._observe_events:
                observer._observe_events[self.name](self)

    def __str__(self):
        return f"{self.name}. New list: [{self.changed}], by/on position {self.posOrRange}, Previous list: [{self.before}]"


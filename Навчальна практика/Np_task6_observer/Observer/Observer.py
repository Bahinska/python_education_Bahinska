from Logger import Logger
class Observer:
    _observers = []

    def __init__(self):
        self._observers.append(self)
        self._observe_events = {}

    def observe_event(self, event_name, callback):
        self._observe_events[event_name] = callback

    def not_observe_event(self, event_name):
        if event_name in self._observe_events.keys():
            del self._observe_events[event_name]
        else:
            raise Exception("This event isn't observed")

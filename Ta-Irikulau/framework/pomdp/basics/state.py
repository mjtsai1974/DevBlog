#from abc import abstractmethod

class State(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        return (
            isinstance(other, State) and
            self.Name == other.Name
        )

    @property
    def Name(self):
        return self._name
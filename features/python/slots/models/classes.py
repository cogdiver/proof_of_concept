

class SinSlots:
    """
    A class without the use of __slots__.

    This class demonstrates the traditional behavior
    of Python classes without the use of __slots__.
    """
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    def attributes_access(self):
        return self.name, self.identifier


class ConSlots:
    """
    A class that utilizes __slots__.

    By defining __slots__, this class explicitly
    declares the attributes it will  handle.
    """
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    def attributes_access(self):
        return self.name, self.identifier

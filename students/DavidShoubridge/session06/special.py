def add_strings():
    """
    Can I use the __add__ magic method to add strings together?
    Currently unable to make it work, needs further research.
    """

    class StringAdd(object):

        def __init__(self, x=None, y=None):
            self.x = x
            self.y = y

        def __add__(self, x, y):
            self.x + self.y

    new_strings = StringAdd("hi")

    more_strings = StringAdd("so")

    print(new_strings + more_strings)

add_strings()

def class_test():
    """
    Will a class method use values given when instancing a new
    object with init?
    No, it will return an error saying class has no attribute "x" unless
    I set attributes x and y outside of the init function.
    """

    class Zulu(object):
        x = 6
        y = 6

        def __init__(self, x, y):
            self.x = x
            self.y = y

        @classmethod
        def add(cls):
            print(cls.x + cls.y)

    kowabunga = Zulu(5, 5)

    kowabunga.add()

class_test()

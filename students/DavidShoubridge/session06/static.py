"Can I use the property of a class in string formatting?"


class Alpha(object):
    def __init__(self, z=8):
        self._z = z

    def _getz(self):
        return self._z

    def _setz(self, value):
        self._z = value

    def _delz(self):
        del self._z
    z = property(_getz, _setz, _delz, doc="docstring")


print("Alpha's value of x is %i." % (Alpha.z))

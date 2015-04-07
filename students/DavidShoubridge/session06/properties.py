def string_format_property():
    """Can I use the property of an object in string formatting?"""

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

    beta = Alpha(20)

    print("Beta's value of z is %i." % (beta._getz()))

    beta._setz(15)

    print("Beta's value of z is now %i." % (beta._getz()))

string_format_property()

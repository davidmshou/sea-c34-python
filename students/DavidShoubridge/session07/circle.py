#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return(u"Circle with radius: %.6f" % (self._radius))

    def __repr__(self):
        return(u"Circle(%i)" % (self._radius))

    def __add__(self, other):
        return(Circle(self._radius + other._radius))

    def __mul__(self, other):
        return(Circle(self._radius * other))

    def __cmp__(self, other):
        return(self._radius - other._radius)

    def __ne__(self, other):
        return(self._radius != other._radius)

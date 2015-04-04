#!/usr/bin/env python
from __future__ import print_function


"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    tag_name = u""
    indentation = u"    "

    def __init__(self, content):
        self.content = content

    def append(self, content):
        pass

    def render(self, file_out, ind=""):

#!/usr/bin/env python
from __future__ import print_function


class Element(object):

    tag_name = u""
    indentation = u"    "

    def __init__(self, content=None):
        self.content = content

    def append(self, content):
        pass

    def render(self, file_out, ind=""):

#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    """HTML element"""
    tag_name = u"html"
    indentation = u"    "

    def __init__(self, content=None):
        if content is True:
            self.content += content
        else:
            self.content = ""

    def append(self, element):
        """Append new string to content."""
        self.content += (self.indentation + str(element))

    def render(self, file_out, ind=""):
        """Render the new element to HTML."""
        file_out.write(self.indentation + "<" + self.tag_name + ">\n"
                       + self.indentation + self.content + "\n"
                       + self.indentation + "</" + self.tag_name + ">")


class Body(Element):
    tag_name = u"Body"


class P(Element):
    tag_name = u"p"

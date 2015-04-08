#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    """HTML element"""
    tag_name = u"html"
    indentation = u"    "

    def __init__(self, content=None):
        if content:
            self.children = [content]
        else:
            self.children = []

    def append(self, element):
        """Append new string to content."""
        self.children.append(element)

    def render(self, file_out, ind=""):
        """Render the new element to HTML."""
        file_out.write(ind + "<" + self.tag_name + ">\n")

        for child in self.children:
            try:
                child.render(file_out, self.indentation + ind)
            except AttributeError:
                file_out.write(self.indentation + ind + unicode(child) + "\n")

        file_out.write(ind + "</" + self.tag_name + ">\n")


class Html(Element):
    """Html element"""
    tag_name = u"html"


class Body(Element):
    """Body element."""
    tag_name = u"body"


class P(Element):
    """Paragraph element."""
    tag_name = u"p"

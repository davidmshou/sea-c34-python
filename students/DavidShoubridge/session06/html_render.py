#!/usr/bin/env python
from __future__ import print_function


class Element(object):
    """Parent element"""
    tag_name = u"html"
    indentation = u"    "

    def __init__(self, content=None, **kwargs):
        if content:
            self.children = [content]
        else:
            self.children = []

        self.attributes = kwargs

        self.attr = ""

        for key, value in self.attributes.items():
            self.attr = " %s=%s" % (key, value)

    def append(self, element):
        """Append new element to content."""
        self.children.append(element)

    def render(self, file_out, ind=u""):
        """Render the new element to HTML."""
        file_out.write(ind + "<" + self.tag_name + self.attr + ">\n")

        for child in self.children:
            try:
                child.render(file_out, self.indentation + ind)
            except AttributeError:
                file_out.write(self.indentation + ind + unicode(child) + "\n")

        file_out.write(ind + "</" + self.tag_name + ">\n")


class Html(Element):
    """Html element"""
    header = u"<!DOCTYPE html>"
    tag_name = u"html"

    def render(self, file_out, ind=u""):
        """Render the new element to HTML."""
        file_out.write(self.header + "\n")
        file_out.write(ind + "<" + self.tag_name + self.attr + ">\n")

        for child in self.children:
            try:
                child.render(file_out, self.indentation + ind)
            except AttributeError:
                file_out.write(self.indentation + ind + unicode(child) + "\n")

        file_out.write(ind + "</" + self.tag_name + ">\n")


class Body(Element):
    """Body element."""
    tag_name = u"body"


class P(Element):
    """Paragraph element."""
    tag_name = u"p"


class Head(Element):
    """Head element."""
    tag_name = u"head"


class OneLineTag(Element):
    """One Line Element."""
    def render(self, file_out, ind=""):
        """Override original render function for one line output."""
        file_out.write(ind + "<" + self.tag_name + self.attr + ">")

        for child in self.children:
            try:
                child.render(file_out, ind="")
            except AttributeError:
                file_out.write(unicode(child))

        file_out.write("</" + self.tag_name + ">\n")


class Title(OneLineTag):
    """Title element."""
    tag_name = u"title"


class SelfClosingTag(Element):
    """A self closing tag."""
    def render(self, file_out, ind=u""):
        """
        Override the render function to render a self-closing tag to HTML.
        """
        file_out.write(ind + "<" + self.tag_name + self.attr + "> \n")


class Hr(SelfClosingTag):
    """An hr tag."""
    tag_name = u"hr /"


class Br(SelfClosingTag):
    """A br tag."""
    tag_name = u"br /"


class A(OneLineTag):
    """'A' tag."""
    tag_name = "a"

    def __init__(self, link, content, **kwargs):
        self.link = link
        self.content = content
        Element.__init__(self, content=None, href=link, **kwargs)


class Ul(Element):
    """Ul tag."""
    tag_name = "ul"


class Li(Element):
    """Li tag."""
    tag_name = "li"


class H(OneLineTag):
    """Header tag."""

    def __init__(self, level, content=None, **kwargs):
        self.tag_name = "h%i" % (level)
        Element.__init__(self, content, **kwargs)


class Meta(SelfClosingTag):
    """Meta tag."""
    tag_name = "meta"

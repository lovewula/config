# encoding: utf-8
# module lxml.etree
# from D:\Python\Python27\lib\site-packages\lxml\etree.pyd
# by generator 1.145
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

from LxmlSyntaxError import LxmlSyntaxError

class ParseError(LxmlSyntaxError):
    """
    Syntax error while parsing an XML document.
    
        For compatibility with ElementTree 1.3 and later.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __qualname__ = 'ParseError'



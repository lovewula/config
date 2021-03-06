# encoding: utf-8
# module lxml.etree
# from D:\Python\Python27\lib\site-packages\lxml\etree.pyd
# by generator 1.145
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

from LxmlError import LxmlError

class DocumentInvalid(LxmlError):
    """
    Validation error.
    
        Raised by all document validators when their ``assertValid(tree)``
        method fails.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __qualname__ = 'DocumentInvalid'



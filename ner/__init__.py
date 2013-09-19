#!/usr/bin/env python

"""Python wrapper for the Stanford NER.
@author Dat Hoang
@date March 2011"""


from .client import (
    SocketNER,
    HttpNER,
)

from .exceptions import (
    NERError,
)

__all__ = [
    'SocketNER',
    'HttpNER',
    'NERError',
]

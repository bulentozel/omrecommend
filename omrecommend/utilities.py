# -*- coding: utf-8 -*-
"""A set of tools developed for general purpose use.

"""
import sys, os
sys.path.insert(0, os.path.abspath('../'))


def get_attributes(pobj):
    """Given any python object returns its data attributes.

    Args:
        pobj (:obj:`Maker`): A python object.

    Returns:
        (:obj:`list` of :obj:`str`): list of attribute names.

    Raises:
        TypeError: Raised if an object type without a __dict__ attribute is given.
    """

    if '__dict__' not in dir(pobj):
        raise TypeError('A Python object with attributes is expected.')

    attrs = {k:v for k,v in pobj.__dict__.items() if not k.startswith('_')}
    return [k for k, v in attrs.items() if type(v) != 'function']



if __name__ == '__main__': pass

# -*- coding: utf-8 -*-

"""
Module that provides useful functions for the quicksort

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2016, january
"""

import random
import numpy as np
from element import *

def is_sorted(t):
    """
    Predicate to test whether an array is sorted in increasing order.

    Args:
      t (NumPy array of Element): An array of Element
    
    Returns:
      bool: `True` if the array is sorted, else `False`

    Examples:
      >>> import numpy    
      >>> is_sorted(numpy.array([1,2,3]))
      True
      >>> is_sorted(numpy.array([1,3,2]))
      False
    """
    n = len(t)
    i = 0
    while i < n-1 and t[i] <= t[i+1]:
        i = i + 1
    return i == n - 1

def decreasing_array(n):
    """
    Creates a fresh array of Elements in decreasing order.
    
    Args:
      n (int): The length of the array

    Returns:
      NumPy array: An array of Element from n-1 to 0

    Example:
      >>> print(decreasing_array(3))
      [2 1 0]
    """
    return np.array([Element(i) for i in reversed(range(n))])


def increasing_array(n):
    """
    Creates a fresh array of Elements in increasing order.
    
    Args:
      n (int): The length of the array

    Returns:
      NumPy array: An array of Element from 0 to n-1

    Example:
      >>> print(increasing_array(3))
      [0 1 2]
    """
    return np.array([Element(i) for i in range(n)])


def random_array(n):
    """
    Creates a fresh array of Elements in pseudo-random order. Each Element from
    0 to n-1 is present only once.
    
    Args:
      n (int): The length of the array

    Returns:
      NumPy array: An array containing Elements between 0 and n-1

    Example:
      >>> sorted(random_array(3))
      [0, 1, 2]
    
    """
    l = [Element(i) for i in range(n)]
    random.shuffle(l)
    return np.array(l)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

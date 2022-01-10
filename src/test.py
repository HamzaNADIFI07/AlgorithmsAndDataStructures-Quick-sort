# -*- coding: utf-8 -*-

"""
Test module for quicksort assignment

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2018, january
"""

import sorting
import generate
import copy
from element import Element

global cpt

def cmp(a,b):
    """
    A comparison function

    Args:
      a (Element): First element    
      b (Element): Second element
    
    Returns:
      int: 0 if a == b, 1 if a > b, -1 if a < b

    Examples:
      >>> from element import Element
      >>> cpt = 0
      >>> cmp(Element(10),Element(5))
      1
      >>> cmp(Element(5),Element(5))
      0
      >>> cmp(Element(5),Element(10))
      -1
    """
    global cpt
    cpt = cpt + 1
    return Element.cmp(a,b)

if __name__ == "__main__":
    cpt = 0

    import doctest
    doctest.testmod()

    t = generate.random_array(30)
    tt = sorting.merge_sort(t,cmp)
    print (tt)
    if generate.is_sorted (tt):
        print("Yes !!") 
    else:
        raise Exception("Array has not been correctly sorted by merge sort")

    t2 = copy.deepcopy(t)
    
    sorting.quicksort(t2,cmp)
    if generate.is_sorted (t2):
        print("Yes !!") 
    else:
        raise Exception("Array has not been correctly sorted by quicksort")

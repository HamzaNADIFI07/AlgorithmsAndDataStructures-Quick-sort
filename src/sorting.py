# -*- coding: utf-8 -*-

"""
Sorting functions module for quicksort assignment

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2018, january
"""

import copy
import random
import numpy as np
import element

def merge (t1,t2, cmp):
    """
    Given two sorted arrays, creates a fresh sorted array.
    
    Args:
      t1 (Array): An array of objects
      t2 (Array): An array of objects
      cmp (function): A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b

    Note: Complexity
          Time complexity of merge is $O(n_1+n_2)$ with
          $n_1$ and $n_2$ resp. the length of `t1` and `t2`

    Returns:
      Array: A fresh array, sorted.
    
    Examples:
      >>> import numpy
      >>> def cmp (x,y): 
      ...    if x == y:
      ...       return 0
      ...    elif x < y:
      ...       return -1
      ...    else:
      ...       return 1
      >>> t1 = numpy.array([0,2,5,6])
      >>> t2 = numpy.array([1,3,4])
      >>> merge(t1,t2,cmp)
      array([0, 1, 2, 3, 4, 5, 6])
    """
    n1 = len(t1)
    n2 = len(t2)
    t = np.zeros(n1+n2,dtype=type(t1[0]))
    i = j = k = 0
    while i < n1 and j < n2:
        if cmp(t1[i],t2[j]) < 0:
            t[k] = t1[i]
            i = i + 1
        else:
            t[k] = t2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        t[k] = t1[i]
        i = i + 1
        k = k + 1
    while j < n2:
        t[k] = t2[j]
        j = j + 1
        k = k + 1
    return t


def merge_sort (t,cmp):
    """
    A sorting function implementing the merge sort algorithm

    Args:
      t (Array): An array of integers
      cmp (function): A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    
    Returns:
      Array: A fresh array, sorted.

    Examples:
      >>> import generate
      >>> def cmp_element (x,y): 
      ...    return x.cmp(y)
      >>> t = generate.random_array(10)
      >>> merge_sort(t,cmp_element)
      array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=object)
    """
    n = len(t)
    if n <= 1:
        # cas de base
        return copy.deepcopy(t)
    else:
        # cas general
        t1 = merge_sort((t[0:((n-1)//2+1)]),cmp)
        t2 = merge_sort((t[((n-1)//2+1):n]),cmp)
        return merge(t1,t2,cmp)
    
def quicksort (t, cmp, pivot_func):
    """
    A sorting function implementing the quicksort algorithm on the whole array `t`.
    
    Args:
      t (Array): An array of Element
      cmp (function: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
      pivot_func (function): A function that returns the pivot index inside a slice.
      
    **Returns:** Nothing

    Note:
          `t` is modified during the sort process

    Warning: Attention
             **ÉCRIRE LES DOCTESTS**
    >>> import numpy
    >>> def cmp (x,y): 
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([5, 6, 1, 3, 4, 9, 8, 2, 7])
    >>> quicksort(t, cmp, random_pivot)
    >>> list(map(int,t))
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    s = {'data':t, 'left':0, 'right':len(t)-1}
    quicksort_slice(s, cmp, pivot_func)


def quicksort_slice (s, cmp, pivot_func):
    """
    A sorting function implementing the quicksort algorithm.
    
    Args:
      s (dict): A slice of an array, that is a dictionary with 3 fields :
                `data`, `left`, `right` representing resp. an array of objects and left
                 and right bounds of the slice.
      cmp (function): A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
      pivot_func (function): A function that returns the pivot index inside a slice.
    **Returns:** Nothing

    Warning: Attention
             **ÉCRIRE LES DOCTESTS**
    >>> import numpy
    >>> def cmp (x,y): 
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> t = numpy.array([5, 6, 1, 3, 4, 9, 8, 2, 7])
    >>> s = {'left': 0, 'right': len(t) - 1, 'data': t}
    >>> quicksort_slice(s, cmp, random_pivot)
    >>> list(map(int,s['data']))
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    
    if s['left'] < s['right']:
        pivot_pos = pivot_func(s)
        (s1, s2) = partition(s, cmp, pivot_pos)
        if s1['left'] < s1['right']:
            quicksort_slice(s1, cmp, pivot_func)
        if s2['left'] < s2['right']:
            quicksort_slice(s2, cmp, pivot_func)

def naive_pivot(s):
    '''
    Args:
      s (dict): A slice of an array, that is a dictionary with 3 fields :
                `data`, `left`, `right` representing resp. an array of objects and left
                 and right bounds of the slice.

    Returns:
      int: a position for the pivot. Systematically returns the first position
           of the slice as a naive choice.

    Examples:
      >>> s = {'data': None, 'left': 2, 'right': 10}
      >>> naive_pivot(s)
      2
      >>> s = {'data': None, 'left': 3, 'right': 10}
      >>> naive_pivot(s)
      3
    '''
    return s['left']

def random_pivot(s):
    """
    Returns a random index between `left` and `right` (inclusive).

    Args:
      s (dict): A dictionary representing a slice of an array, containing:
                - "left": left bound,
                - "right": right bound.

    Returns:
      int: A random integer between `s['left']` and `s['right']`.

    Examples:
      >>> import random
      >>> random.seed(42)
      >>> s = {'left': 2, 'right': 10}
      >>> random_pivot(s) in range(s['left'], s['right'] + 1)
      True

      >>> s = {'left': 0, 'right': 5}
      >>> pivot = random_pivot(s)
      >>> s['left'] <= pivot <= s['right']
      True
      """
      
    left_index=s['left']
    right_index=s['right']
    return random.randint(left_index, right_index)  


def partition (s, cmp, pivot_pos):
    """
    Creates two slices from `s` by selecting in the first slice all
    elements that are lower than the pivot and in the second one all the other
    elements.

    Args:
      s (dict): A slice represented as a dictionary with 3 fields :

          * `data`: the array of objects,
          * `left`: left bound of the slice (a position in the array),
          * `right`: right bound of the slice.
      cmp (function): A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
      pivot_pos (int): The position at which we take the pivot in `s['data']`

    Returns:
      tuple: A couple of slices, the first slice contains all elements that are 
      less than the pivot, the second one contains all elements that are 
      greater than the pivot, the pivot does not belong to any slice.
      At the end, in the array the pivot is after the left slice and before 
      the right slice.

    Examples:
      >>> import generate
      >>> import element
      >>> import numpy
      >>> def cmp (x,y): 
      ...    if x == y:
      ...       return 0
      ...    elif x < y:
      ...       return -1
      ...    else:
      ...       return 1
      >>> t = numpy.array([element.Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
      >>> p = {'left':0,'right':len(t)-1,'data':t}
      >>> p1,p2 = partition(p,cmp,0)
      >>> list(p1['data'][p1['left']:p1['right']+1])
      [4, 2, 1, 3]
      >>> list(p2['data'][p2['left']:p2['right']+1])
      [9, 8, 6, 7]
      >>> t = numpy.array([2, 1])
      >>> p = {'left': 0, 'right': len(t) - 1, 'data': t}
      >>> p1, p2 = partition(p, cmp, 0)  # Pivot = 2
      >>> list(map(int, p1['data'][p1['left']:p1['right'] + 1]))
      [1]
      >>> list(p2['data'][p2['left']:p2['right'] + 1])
      []

  
    Warning: Attention
             **FINIR D'ÉCRIRE LES DOCTESTS**

             * Remplacer `None` par la valeur attendue
             * Rajouter des tests
    """
    data = s['data']
    left, right = s['left'], s['right']
    pivot = data[pivot_pos]

    data[left], data[pivot_pos] = data[pivot_pos], data[left]

    i, j = left + 1, right

    while i <= j:
        while i <= j and cmp(data[i], pivot) < 0:
            i += 1
        while i <= j and cmp(data[j], pivot) > 0:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

    data[left], data[j] = data[j], data[left]

    return {"data": data, "left": left, "right": j - 1}, {"data": data, "left": j + 1, "right": right}

def optimal_pivot(s):
    """
    Returns the index of the median element in the slice.

    Examples:
      >>> s = {'data': [5, 1, 9, 3, 7], 'left': 0, 'right': 4}
      >>> optimal_pivot(s)
      2
      >>> s = {'data': [10, 20, 30, 40, 50], 'left': 1, 'right': 3}
      >>> optimal_pivot(s)
      2
    """
    return s['left'] + (s['right'] - s['left']) // 2

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True) # "verbose=True" pour afficher la trace des tests qui passent


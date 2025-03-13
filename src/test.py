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

def random_100():
    """
    Runs sorting benchmarks on arrays of sizes 1 to 100 with 100 trials each.
    Stores the average number of comparisons for:
    - Merge Sort
    - QuickSort (naive pivot)
    - QuickSort (random pivot)
    
    The results are written to `random_100.dat`
    """
    with open("random_100.dat", "w") as file:
        for size in range(1, 101):
            global cpt
            merge_total = 0
            quick_naive_total = 0
            quick_random_total = 0

            for i in range(100):
                array1 = generate.random_array(size)
                array2 = copy.deepcopy(array1)
                array3 = copy.deepcopy(array1)

                cpt = 0
                sorting.merge_sort(array1, cmp)
                merge_total += cpt

                cpt = 0
                sorting.quicksort(array2, cmp, sorting.naive_pivot)
                quick_naive_total += cpt

                cpt = 0
                sorting.quicksort(array3, cmp, sorting.random_pivot)
                quick_random_total += cpt

            avg_merge = merge_total / 100
            avg_quick_naive = quick_naive_total / 100
            avg_quick_random = quick_random_total / 100

            file.write(f"{size} {avg_merge:.2f} {avg_quick_naive:.2f} {avg_quick_random:.2f}\n")

def increasing_100():
    """
    Runs sorting benchmarks on **increasing** arrays (sorted order) of sizes 1 to 100.
    Stores the average number of comparisons for:
    - MergeSort
    - QuickSort (naive pivot)
    - QuickSort (random pivot)
    
    Results are written to `increasing_100.dat`.
    """
    with open("increasing_100.dat", "w") as file:

        for size in range(1, 101):
            global cpt
            merge_total = 0
            quick_naive_total = 0
            quick_random_total = 0

            for i in range(100):
                array1 = generate.increasing_array(size)
                array2 = copy.deepcopy(array1)
                array3 = copy.deepcopy(array1)

                cpt = 0
                sorting.merge_sort(array1, cmp)
                merge_total += cpt

                cpt = 0
                sorting.quicksort(array2, cmp, sorting.naive_pivot)
                quick_naive_total += cpt

                cpt = 0
                sorting.quicksort(array3, cmp, sorting.random_pivot)
                quick_random_total += cpt

            avg_merge = merge_total / 100
            avg_quick_naive = quick_naive_total / 100
            avg_quick_random = quick_random_total / 100

            file.write(f"{size} {avg_merge:.2f} {avg_quick_naive:.2f} {avg_quick_random:.2f}\n")



if __name__ == "__main__":
    cpt = 0

    import doctest
    doctest.testmod()

    t = generate.random_array(30)
    tt = sorting.merge_sort(t,cmp)
    print (tt)
    if generate.is_sorted (tt):
        print("Yes !!") 
        print("Nombre de comparaison du tri fusion: ", cpt)
    else:
        raise Exception("Array has not been correctly sorted by merge sort")

    t2 = copy.deepcopy(t)
    cpt = 0
    sorting.quicksort(t2,cmp, sorting.random_pivot)
    # sorting.quicksort(t2,cmp)
    if generate.is_sorted (t2):
        print("Yes !!") 
        print("Nombre de comparaison du tri rapide: ", cpt)
    else:
        raise Exception("Array has not been correctly sorted by quicksort")
    #random_100()
    increasing_100()
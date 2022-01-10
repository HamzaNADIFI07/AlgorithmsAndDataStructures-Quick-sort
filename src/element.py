import time
from functools import total_ordering

@total_ordering
class Element:
    '''
    An Element has a value and can be compared to another Element.
    '''

    def __init__(self,value):
        assert(type(value) == int)
        self.value = value

    def __add__ (self, other):
        return Element(self.value + other.value)
    
    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return "{}".format(self.value)

    def cmp (self,other):
        """
        Compares this element and `other`.

        Args:
          other (Element): The other Element

        Returns:
          int: -1, 0 or 1 resp. if `self < other`, `self` = `other` or `self` > `other`

        Examples:
          >>> Element(45).cmp(Element(234))
          -1
          >>> Element(45).cmp(Element(45))
          0
          >>> Element(45).cmp(Element(24))
          1
        """
        if self.value == other.value:
            return 0
        elif self.value < other.value:
            return -1
        else:
            return 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
        

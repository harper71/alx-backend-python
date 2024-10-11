#!/usr/bin/ env python3
"""corrects the code"""

from typing import List, Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that takes a list lst as argument
    and returns its first element if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None

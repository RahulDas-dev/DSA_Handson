"""How to Flatten a List of Lists
Types of Nested Lists
1. Regular List of Lists ex- [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
2. Irregular List of Lists ex - [[1, 2, 3], [4, 5], 6]
"""

from typing import Iterator, List


def flatten_list(l1: List) -> Iterator:
    for item in l1:
        if isinstance(item, list):
            yield from flatten_list(item)
        else:
            yield item

from datetime import datetime, timedelta
from itertools import zip_longest
from typing import Iterator, List, Union

# Iterating over every two elements in a list
n_item_ierator = lambda l1, n: zip_longest(*[iter(l1)] * n)

# OR


def n_item_groupped(l1: Union[List, Iterator], n: int) -> Iterator:
    """Returns iterartor ,which yield n items from given List"""
    return zip_longest(*[iter(l1)] * n)


# Date Range Itrator,
class DateIteraor:
    def __init__(self, initail_date: datetime, duration: int):
        self.inital_date = initail_date
        self.current_date = initail_date
        self.final_date = self.inital_date - timedelta(days=duration)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_date > self.final_date:
            self.current_date -= timedelta(days=1)
            return self.current_date
        else:
            raise StopIteration

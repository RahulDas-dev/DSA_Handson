from collections import defaultdict
from operator import itemgetter
from typing import Dict, List


def join_list_of_dicts(l1: List[Dict], l2: List[Dict], dict_key: str = "index") -> List[Dict]:
    """
    Given n lists with m dictionaries as their elements, code will return a new list,
    with a joined set of dictionaries.
    Each dictionary is guaranteed to have a key called 'index'

    l1 = [{'index':1, 'b':2}, {'index':2, 'b':3}, {'index':3, 'green':'eggs'}]
    l2 = [{'index':1, 'c':4}, {'index':2, 'c':5}]
    >>> join_list_of_dicts(l1,l2)
    [{'index':1, 'b':2, 'c':4}, {'index':2, 'b':3, 'c':5}, {'index':3, 'green':'eggs'}]
    """
    temp = defaultdict(dict)
    for item in l1 + l2:
        temp[item[dict_key]].update(item)

    new_list = sorted(temp.values(), key=itemgetter(dict_key), reverse=False)
    return new_list


# Merge dicts, collecting all values
def join_dicts_values_as_list(d1: Dict, d2: Dict) -> Dict:
    """Given with 2 dictionaries code will return a new dict values will be list,
    d1 = {'pig':1, 'cow':2, 'parrot':3, 'monkey':4}
    d2 = {'pig':5, 'cow':8, 'parrot':5, 'dog':4}
    >>join_dicts_values_as_list(d1,d2)
    {'pig':[1,5], 'cow':[2,8], 'parrot':[3,5], 'monkey':[4],'dog':[4]}
    """
    temp = defaultdict(list)
    for key, value in list(d1.items()) + list(d2.items()):
        temp[key].append(value)
    return temp

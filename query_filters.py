import re
from typing import Iterable, Set, List


def filter_data(param: str, data: str) -> Iterable[str]:
    return filter(lambda x: param in x, data)


def map_data(param: int, data: str) -> Iterable[str]:
    number_colom = int(param)
    return map(lambda x: x.split(' ')[number_colom], data)


def unique_data(data: str, param = None) -> Set[str]:
    return set(data)


def sorted_data(param: str, data: str) -> List[str]:
    return sorted(data, reverse=param == 'desc')


def limit_data(param: str, data: str) -> List[str]:
    limit_num = int(param)
    return list(data)[:limit_num]


def regex_data(param, data) -> Iterable[str]:
    regex = re.compile(param)
    return [row for row in data if regex.search(row)]

def filter_data(param, data):
    return filter(lambda x: param in x, data)


def map_data(param, data):
    number_colom = int(param)
    return map(lambda x: x.split(' ')[number_colom], data)


def unique_data(data: str):
    return set(data)


def sorted_data(param: str, data: str):
    return sorted(data, reverse=param == 'desc')


def limit_data(param: str, data: str):
    limit_num = int(param)
    return list(data)[:limit_num]

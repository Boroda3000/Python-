data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calc_list(list_):
    sum_ = 0
    for i in list_:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, list):
            sum_ += calc_list(i)
        elif isinstance(i, dict):
            sum_ += calc_dict(i)
        elif isinstance(i, tuple):
            sum_ += calc_tuple(i)
    return sum_


def calc_dict(dict_):
    sum_ = 0
    for key, value in dict_.items():
        sum_ += calc_key(key)
        sum_ += calc_value(value)
    return sum_


def calc_key(key):
    sum_key = 0
    if isinstance(key, int):
        sum_key += key
    elif isinstance(key, str):
        sum_key += len(key)
    elif isinstance(key, list):
        sum_key += calc_list(key)
    elif isinstance(key, dict):
        sum_key += calc_dict(key)
    elif isinstance(key, tuple):
        sum_key += calc_tuple(key)
    elif isinstance(key, set):
        sum_key += calc_set(key)
    return sum_key


def calc_value(value):
    sum_value = 0
    if isinstance(value, int):
        sum_value += value
    elif isinstance(value, str):
        sum_value += len(value)
    elif isinstance(value, list):
        sum_value += calc_list(value)
    elif isinstance(value, dict):
        sum_value += calc_dict(value)
    elif isinstance(value, tuple):
        sum_value += calc_tuple(value)
    elif isinstance(value, set):
        sum_value += calc_set(value)
    return sum_value


def calc_tuple(tup):
    sum_ = 0
    for i in tup:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, list):
            sum_ += calc_list(i)
        elif isinstance(i, dict):
            sum_ += calc_dict(i)
        elif isinstance(i, tuple):
            sum_ += calc_tuple(i)
    return sum_


def calc_set(set_):
    sum_ = 0
    for i in set_:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, list):
            sum_ += calc_list(i)
        elif isinstance(i, dict):
            sum_ += calc_dict(i)
        elif isinstance(i, tuple):
            sum_ += calc_tuple(i)
        elif isinstance(i, set):
            sum_ += calc_set(i)
    return sum_


def calculate_structure_sum(func):
    sum_ = 0
    for i in func:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, list):
            sum_ += calc_list(i)
        elif isinstance(i, dict):
            sum_ += calc_dict(i)
        elif isinstance(i, tuple):
            sum_ += calc_tuple(i)
        elif isinstance(i, set):
            sum_ += calc_set(i)
    return sum_


result = calculate_structure_sum(data_structure)
print(result)